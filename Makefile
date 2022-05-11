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
	rm -rf figures/* tables/* _build/*

# run all the notebooks
.PHONY: all
all:
	jupyter execute codes/* --kernel_name=hw07
	jupyter execute main.ipynb --kernel_name=hw07