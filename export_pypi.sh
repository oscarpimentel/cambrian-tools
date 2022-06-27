#!/bin/bash
source ~/.bashrc
reset

# enter environment
# env_name="env_name"
env_name=${PWD##*/}
conda activate $env_name
conda env list
python --version

# get version
old_version=$(head -n 1 version)
python create_version_file.py --version $old_version --increase_simple_version
version=$(head -n 1 version)
echo exporting version $version

# export to pypi
rm -rf ./dist
rm -rf *.egg-info
pip install twine
python setup.py sdist
twine upload dist/* -u opimentel-pypi
