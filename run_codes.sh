#!/bin/bash -i

	jupyter execute codes/data_prepare.ipynb --kernel_name=hw07
	jupyter execute codes/data_visual.ipynb --kernel_name=hw07
    
	jupyter execute codes/logistic_reg.ipynb --kernel_name=hw07
    
	jupyter execute codes/decision_tree_and_random_forest.ipynb --kernel_name=hw07
    
	jupyter execute codes/final_model_selection.ipynb --kernel_name=hw07
    
	jupyter execute codes/two_populations_analysis.ipynb --kernel_name=hw07
    
	jupyter execute main.ipynb --kernel_name=hw07
    