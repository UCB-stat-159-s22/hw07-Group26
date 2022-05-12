# A Study of a Breast Cancer Dataset

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw07-Group26/main?labpath=main.ipynb)

Github Pages [here](https://ucb-stat-159-s22.github.io/hw07-Group26/)

Authors: Kshitij (TJ) Chauhan, Neha Haq, Wenhao Pan, Jiaji Wu

## Introduction

This repository includes a study of a breast bancer dataset that is downloaded from [Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)

As a group, we wanted to focus on the health industry. We decided to look at cancer, as cancer is a widely studied disease today. This motivated us to analyze the breast cancer dataset publicly available on Kaggle. We believe that our analysis of this dataset would be helpful to doctors and patients, who want to find out whether the cancer is benign or malignant.

For our model, we decided to choose to use a classification model as our goal is to classify whether the cancer is benign or malignant. To do this, we ran different models including logistic regression, decision trees and random forests and then, based on the performance on the vailidation set, we picked the best one. Based on our final model, we hope that our model can serve as a strong basis for predicting whether the cancer is benign or malignant based on its characteristics. Furthermore, we performed hypothesis testing using the parametric Two-Sample T-Test and the non-parametric Wilcoxian Rank Sumt Test to see whether our results are statistically significant at a significance level of 5%. 

## Installation

Run `make env` to setup the conda environment and install the required dependencies. Use `hw07` kernel to execute the Jupyter Notebook. 

## Repository Structure

- `data/` contains different datasets in csv formats
  - `raw_data.csv` is the original data downloaded from Kaggle
  - `clean.csv` is the cleaned version of `raw_data.csv`
  - `train.csv` is the training dataset 
  - `val.csv` is the validation dataset
  - `test.csv` is the testing dataset
- `figures/` contains generated figures from running the notebooks in `codes/`
- `tables/` contains generated tables from running the notebooks in `codes/`
- `codes/` contains the jupyter notebooks for data analysis
  - `data_prepare.ipynb` prepares the data for later analysis
  - `data_visual.ipynb` conducts EDA
  - `logistic_reg.ipynb` conducts logistic regression analysis
  - `decision_tree_and_random_forest.ipynb` conducts decision tree and random forest modeling and comparison
  - `final_model_selection.ipynb` chooses final model between LR and RF
  - `two_populations_analysis.ipynb` conducts two sample hypothesis testing
- `models/` contains different fitted models from running the notebooks in `codes/`
  - `dt_model.sav` is the fitted decesion tree model
  - `rf_model.sav` is the fitted random forest model
  - `lg_model.sav` is the fitted logistic regression model
- `diagnosis/` contains required files for package creation purposes.
  - `README.md` info of package
  - `setup.py` required to create python package
  - `pyproj.tml` required to create python package
  - `setup.cfg` required to create python package
  - `LICENSE` info of package
  - `diagnosis/` contains content of package
    - `tests/` tests for created methods
    - `__init__.py` required to create python package
    - `modelmake.py` methods for decision tree modeling
    - `twosample.py` methods for hypothesis testing
    - `main.py` methods for plotting figures
    - `prepare.py` methods for preparing the datad
- `_config.yml` required for JupyterBook
- `conf.py` required for JupyterBook
- `_toc.yml` is the table of contents for JupyterBook
- `book-requirements.txt` packages for the book build in Github Actions
- `environment.yml` hw07 conda environment installation
- `envsetup.sh` utilized by `make env`
- `envupdate.sh` utilized by `make update`
- `envremove.sh` utilized by `make remove`
- `run_codes.sh` utilized by `make all`
- `html_hub.sh` build JupyterBook to view it on the hub with the URL proxy trick 
- `Makefile` make commands for easy execution
- `LICENSE` contains the license used by the repo
- `README.md` current document
- `requirements.txt` command to install diagnosis python package
- `main.ipynb` summarizes and discusses the findings and outcomes of our analysis
- `hw07-description.ipynb` Stat 159 HW7 assignment desctiption

## Makefile Commands

`make`
- `env` creates and configures the environment
- `remove-env` remove the environment
- `update-env` update the environment
- `html` build the JupyterBook normally
- `html-hub` build the JupyterBook so that you can view it on the hub with the URL proxy trick: https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html
- `clean` clean up the generated figures, tables, data, and _build folders.
- `all` run all the notebooks

## Notes

- When using `pytest` to test the functions in the package, you need to call `pytest diagnosis` in the root directory, i.e., in `hw07-Group26`, run `pytest diagnosis` in the terminal. Also, since our testing functions use some generated data, make sure running `make all` to generated all neccessary files before testing.

