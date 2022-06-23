#!/bin/bash
source ~/.bashrc
git init
rm .gitignore
echo '*.secrets*' >> .gitignore
echo '*.pyc*' >> .gitignore
echo '*.ipynb_checkpoints*' >> .gitignore
echo '*__pycache__*' >> .gitignore
echo '.vscode/' >> .gitignore
echo 'temp/' >> .gitignore
echo 'save/' >> .gitignore
echo 'data/' >> .gitignore
echo 'debug/' >> .gitignore
echo 'dist/' >> .gitignore
repo_name=${PWD##*/}
env_name=$repo_name
conda deactivate
conda create -n $env_name python=3.10 -y
conda activate $env_name