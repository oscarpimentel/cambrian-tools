#!/bin/bash
source ~/.bashrc
reset

# init
git init

# create .gitignore
rm .gitignore
echo '*.secrets*' >> .gitignore
echo '*.pyc*' >> .gitignore
echo '*.ipynb_checkpoints*' >> .gitignore
echo '*__pycache__*' >> .gitignore
echo '*.vscode*' >> .gitignore
echo '*.egg-info*' >> .gitignore
echo 'temp/' >> .gitignore
echo 'save/' >> .gitignore
echo 'data/' >> .gitignore
echo 'debug/' >> .gitignore
echo 'dist/' >> .gitignore

# create env
repo_name=${PWD##*/}
env_name=$repo_name
conda deactivate
conda create -n $env_name python=3.10 -y

# install nbstripout
conda activate $env_name
conda install -c conda-forge nbstripout -y
nbstripout --install
nbstripout --status
echo "========================================================================="
echo "enter the new environment by using: conda activate $env_name"