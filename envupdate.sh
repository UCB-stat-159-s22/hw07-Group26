#!/bin/bash -i

mamba env update --file environment.yml --prune
conda activate hw07
python -m ipykernel install --user --name hw07 --display-name "hw07"