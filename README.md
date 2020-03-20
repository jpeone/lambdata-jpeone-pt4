# lambdata-jpeone-pt4
This is an MVP, and honestly a hot mess.

A practice package exploring the following
* pipenv - managing virtual environments and making packages
* python modules
* publishing packages to PyPi
* Pep8 style
* oop - creating classes, methods, properties and exploring inheritance
* Docker containers
* Unit testing

## Installation
#### Dependencies
Requires numpy, pandas and scikit-learn  
#### Instructions
1. install numpy ```pip install numpy```
2. install pandas ```pip install pandas```
3. install scikit-learn ```pip install scikit-learn```
4. install lambdata 
```pip install -i https://test.pypi.org/simple/ lambdata-jpeone-pt4```

## Usage
```python
from lambdata.assignment import CustomFrame
from lambdata.my_mod import Helper

helper = Helper()

#the enlarge method
enbiggen = helper.enlarge(5)

#the tocol method
df2 = helper.tocol(df, [7, 8, 9], 'z')

#train_val_test_split
X_train, X_val, X_test, y_train, y_val, y_test = helper.train_val_test_split(
    X, y, stratify=y)

#CustomFrame inherits pandas DataFrame
cdf = CustomFrame({"abbrev": ['ca', 'ct', 'co', 'tx', 'dc']})

#the add_state_name method
cdf.add_stat_name()
```
