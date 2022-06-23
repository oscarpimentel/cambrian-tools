#!/bin/bash
source ~/.bashrc
env_name=${PWD##*/}
conda activate $env_name
rm requirements.txt
pip freeze > requirements.txt
rm environment.yml
conda env export > environment.yml