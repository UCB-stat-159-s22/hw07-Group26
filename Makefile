# creates and configures the environment
.PHONY: env
env:
	bash -i envsetup.sh

# remove the environment
.PHONY: remove-env
remove-env:
	bash -i envremove.sh

# update the environment
.PHONY: update-env
update-env:
	bash -i envupdate.sh
    
# build the JupyterBook normally
.PHONY: html
html:
	jupyter-book build .

# build the JupyterBook so that you can view it on the hub with the URL proxy trick as indicated above
.PHONY: html-hub
html-hub:
	bash -i html_hub.sh

# clean up the generated figures, tables and _build folders.
.PHONY: clean
clean:
	rm -rf figures/* tables/* _build/* models/*
	cd figures && touch .gitkeep   
	cd tables && touch .gitkeep
	cd models && touch .gitkeep   
	cd data && rm clean.csv && rm train.csv && rm val.csv && rm test.csv     

# run all the notebooks
.PHONY: all
all:
	bash -i run_codes.sh