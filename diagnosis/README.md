# Information
This package is useful for developing decision tree classification models and conducting two sample parametric and non-parametric hypothesis testing for binary-labeled data. Specifically, this package was created with the intention of being utilized on diagnosing breast cancer patients with either malignant (1) or benign (0) cancer. However, this package may be used for other classifications as well, beyond breast cancer. 

# Installation
To install the package, please execute `pip install diagnosis/.` from the root of the diirectory.

# Notes
We have created tests to properly test the functionality of our methods. Please feel free to refer to the tests folder for examples on executing the methods. 

# Structure
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