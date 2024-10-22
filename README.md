[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/geoocean%2Fcourses%2Fwaves/HEAD?urlpath=tree/)

# BEACH

Fernando J. Méndez Incera (fernando.mendez@unican.es)\
Laura Cagigal (laura.cagigal@unican.es)\
Jared Ortiz-Angulo Cantos (jared.ortizangulo@unican.es)

<a name="ins"></a>
## Data download
- - -
Data can be found in moodle

<a name="ins"></a>
## Install
- - -
<a name="ins_src"></a>
### Create an environment in conda

1. Install Anaconda: ["ANACONDA"](https://www.anaconda.com/download)

2. To run the toolbox, you need to set up a conda enviroment with the required Python packages.

Option 1: 

i. Open a terminal with conda activated
- Windows: "Anaconda prompt"
- Mac: "Terminal" (Automatically detects conda)

ii. Change to the Beach directory:
	`cd BeachEngineering_2023` command
	
iii. Libaries installation: 
- Windows: `conda env create -f environment.yml` command
- Mac: `conda env create environment.yml` command

Option 2:

i. From the Start menu, click the Anaconda Navigator desktop app

ii. On Navigator’s Home tab, in the Environments panel on the left, click over the play button on the `base` enviroment and launch the Anaconda Prompt

iii. By using the `cd` command, navigate to the `BeachEngineering_2023` folder where it is contained this repository and execute: 

```
# Default install, miss some dependencies and functionality
conda env create -f environment.yml 
```

### Activate conda environment
Activate the environment:

```
conda activate beach
```

To remove an environment, in your terminal window or an Anaconda Prompt, run:
```
conda remove --name beach --all
```

### Launch Jupyter Notebook
```
jupyter notebook
```
