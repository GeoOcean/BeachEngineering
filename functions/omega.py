# /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def fallvelocity(D, Tw):
    
    # D = 0.002  # Tamaño de grano [m]
    # Tw = 20    # Temperatura en grados Celsius [º]
    
    # Convertir el tamaño de grano a centímetros
    D = D * 100

    ROWs = 2.75  # Densidad de la arena (Mark 2.75, Kristen, 2.65?)
    g = 981  # Gravedad cm/s^2

    T = [5, 10, 15, 20, 25]
    v = [0.0157, 0.0135, 0.0119, 0.0105, 0.0095]
    ROW = [1.028, 1.027, 1.026, 1.025, 1.024]

    # Interpolación lineal para obtener vw y ROWw
    vw = np.interp(Tw, T, v)
    ROWw = np.interp(Tw, T, ROW)

    A = ((ROWs - ROWw) * g * (D**3)) / (ROWw * (vw**2))

    if A < 39:
        w = ((ROWs - ROWw) * g * (D**2)) / (18 * ROWw * vw)
    else:
        if A < 10**4:
            w = ((((ROWs - ROWw) * g / ROWw)**0.7) * (D**1.1)) / (6 * (vw**0.4))
        else:
            w = np.sqrt(((ROWs - ROWw) * g * D) / (0.91 * ROWw))

    # Convertir a SI (m/s)
    w = w / 100

    return w


def omega_calculation(df, w):
    
    omega=df["H1_Goda"]/(w*df["Tp"])
    df['Omega'] = omega     
    return(df)



def WS85Filter(omega, D, phi, dt):
    # Convert dt from seconds to days
    dt = dt # days!   # original code: dt / 3600 / 24
    
    # Convert D and phi from days to the number of data points
    D = round(D / dt)
    phi = round(phi / dt)
    
    # Initialize the filtered omega array
    omega = np.flipud(omega)
    omegaFiltered = np.empty_like(omega)
    
    # Loop through the omega array
    for jj in range(len(omega) - D):
        T1 = np.zeros(D)
        T2 = np.zeros(D)
        
        # Calculate T1 and T2
        for ii in range(D):
            T1[ii] = 10 ** (-ii / phi)
            T2[ii] = omega[jj + ii] * T1[ii]
        
        # Calculate the filtered value for omega
        omegaFiltered[jj] = np.sum(T2) / np.sum(T1)
    
    # Flip the filtered omega array back
    omegaFiltered = np.flipud(omegaFiltered)
    
    # round
    omegaFiltered = np.round(omegaFiltered, 2)
    
    
    return omegaFiltered






