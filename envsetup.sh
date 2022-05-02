#!/bin/bash -i

mamba env create -f environment.yml -p ~/envs/hw07
conda activate hw07
python -m ipykernel install --user --name hw07 --display-name "hw07"