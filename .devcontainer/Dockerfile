FROM mcr.microsoft.com/devcontainers/miniconda:1-3

# Install mamba (fast solver)
RUN conda install -n base -c conda-forge mamba -y

# Enforce strict channel priority and remove defaults
RUN conda config --set channel_priority strict \
    && conda config --remove channels defaults || true

# Copy environment file
COPY environment.yml /tmp/environment.yml

# Create the beach environment using mamba (DO NOT update base)
RUN mamba env create -f /tmp/environment.yml \
    && conda clean -afy \
    && rm /tmp/environment.yml

# Make beach the default environment
ENV CONDA_DEFAULT_ENV=beach
ENV PATH=/opt/conda/envs/beach/bin:$PATH
