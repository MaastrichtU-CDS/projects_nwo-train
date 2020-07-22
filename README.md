# NWO-TRAIN

## Prototype deployment of IKNL-like Personal Health Train infrastructure.

### Requirements
VM or real box containing (preferred) Ubuntu 18.04 LTS.

At least 16GB RAM.

At least 1 GPU if at all possible.

Fast access storage of at least 20GB but as much as possible - more is always better.

### Docker Community Edition

Install Docker Engine relevant to your machine, it should be one of these here. Ubuntu is recommended but use whatever you prefer.


Windows 10 : https://docs.docker.com/docker-for-windows/install/
Ubuntu : https://docs.docker.com/install/linux/docker-ce/ubuntu/
Mac OS : https://docs.docker.com/docker-for-mac/install/


Set up docker with the instructions from docs.docker.com and then confirm that the simple hello-docker application works.


### python

We need a minimum of version 3.6 or higher. For windows, we recommend the Anaconda version. In Ubuntu, it does not seem to matter much so take the version that comes with Ubuntu.

### ppDLI installation


### atomCAT docker-compose (optional)

The docker-compose.yml file in the atomCAT folder will spin up local instances of pgAdmin4, postgreSQL, juPyter notebook, R2RML and GraphDB all in one single deployment.

### XNAT docker instance

For a local imaging repository we will use XNAT running as another docker. This will facility deep learning and radiomics for imaging.
The version we will use is this [one](https://github.com/NrgXnat/xnat-docker-compose). Bugs with port 22 conflict and postgres superuser unspecified appear to have been repaired as of July 2020.







Install python 3.6 upwards. If using Windows, recommend that you use install from Anaconda and do all the steps from an Anaconda python command window.


Install the ppDLI libraries.


Windows 10 (in anaconda command window) :
mkdir ~/venv
python3 -m venv ~/venv/ppDLI (or maybe just python -m venv ~/venv/ppDLI)
source ~/venv/ppDLI/bin/activate
pip install ppdli
Ubuntu (a few more intermediate steps needed) :
sudo apt-get update
sudo apt-get install git python3-venv python3-pip python3-dev postgresql gcc libpq-dev
mkdir ~/venv
python3 -m venv ~/venv/ppDLI
source ~/venv/ppDLI/bin/activate
pip install --upgrade pip
pip install psycopg2==2.7.7
pip install ppdli
====== ONLY FOR SERVER SIDE INSTALL (not relevant to most) =====
====== ppDLI install commands & server-side configuration given by J van Soest =====
https://gitlab.com/PersonalHealthTrain/implementations/dutchmaastricht/ppdli-configuration
====== Node-side & configuration given by J van Soest =====
Activate the environment you created during the install, see above steps for installing ppDLI library.
It may be that you did not create an environment for the install, it should still work :
(unless already created a configuration file for the node) ppnode new
Give your node configuration an understandable label eg my-config-for-atomCAT.
Enter the api-key given to you by the server operator (you must contact the server operator).
Enter the base-URL of the server (eg http://13.94.188.17)
Enter port to which the server listens: 5000
Path of the api: /api
Database path:?
Defaults for the rest are fine.
(to start broadcasting as the node) ppnode start
(then select which node configuration you want to connect with eg my-config-for-atomCAT)
(if you want to see where ppDLI keeps your configs) ppnode files
(if you just want to see the help page) ppnode
You should now be able to contact the server operator and check if you are connected. A researcher can poll the server
and ask your node to pull a test docker from dockerhub to run (for example, the old fashioned hello-world docker).