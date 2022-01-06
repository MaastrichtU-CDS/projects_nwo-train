# NWO-TRAIN

## DATA STATIONS (DATA NODE) git branch

This branch is for the setup of the data stations inside the partner clinics. 

### System requirements for node
Standalone VM or physical box containing (preferred) Ubuntu 20.04 LTS as operating system, ideally kept separate from direct contact with your production/clinical systems.

Docker Community Edition relevant for your machine.

At least 16GB RAM of working RAM.

Fast access storage (eg ssd) of approximately 250GB but of course more is always better.

Local and (ideally) static internal IP address to receive data incoming from inside the hospital via HTTP or HTTPS.

DICOM export/push is possible from internal radiotherapy treatment planning system towards the abovementioned IP address.

(optional) 1 NVIDIA GPU chip with 8GB or more of internal memory.

Clinical researcher needs to have local admin rights on this node machine to install software and run applications

### Install Docker Community Edition (latest stable version)

Install Docker Engine relevant to your machine, it should be one of these below. Ubuntu is preferred but use whatever fits your system.

[Windows 10](https://docs.docker.com/docker-for-windows/install/)

[Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

[Mac OS](https://docs.docker.com/docker-for-mac/install/)

Set up docker with the instructions from [docs.docker.com](docs.docker.com).

Check the installation is fine by running the simple test ```docker run hello-world```.

Remember to install the ***docker-compose modu;e*** as well - it is sometimes missed from the basic install instructions.

### Install Clinical Trial Processor (Dicom Anonymizer) client application on node machine


### Install XNAT and Python docker container

To begin with, we will set up a docker container that has the following components :

XNAT DICOM Repository - for general documentation see [XNAT](https://www.xnat.org/) and [xnat-docker-compose](https://github.com/NrgXnat/xnat-docker-compose)

Jupyter notebooks


### ppDLI installation

#### Windows 10 (in anaconda command window) :
mkdir ~/venv

python3 -m venv ~/venv/ppDLI (or maybe just python -m venv ~/venv/ppDLI)

source ~/venv/ppDLI/bin/activate

pip install ppdli

#### Ubuntu (a few more intermediate steps needed) :
sudo apt-get update

sudo apt-get install git python3-venv python3-pip python3-dev postgresql gcc libpq-dev

mkdir ~/venv

python3 -m venv ~/venv/ppDLI

source ~/venv/ppDLI/bin/activate

pip install --upgrade pip

pip install psycopg2==2.7.7

pip install ppdli


### ppDLI node-side configuration thanks to Johan van Soest
Activate the environment you created during the install, see above steps for installing ppDLI library.

It may be that you did not create an environment for the install, it should still work :

ppnode new (unless already created a configuration file for the node)

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

### atomCAT docker-compose (optional)

The docker-compose.yml file in the atomCAT folder will spin up local instances of pgAdmin4, postgreSQL, juPyter notebook, R2RML and GraphDB all in one single deployment.

### Radiomics (O-RAW)

More to follow later.

### XNAT docker instance

For a local imaging repository we will use XNAT running as another docker. This will facility deep learning and radiomics for imaging.
The version we will use is this [one](https://github.com/NrgXnat/xnat-docker-compose). Bugs with port 22 conflict and postgres superuser unspecified appear to have been repaired as of July 2020.


