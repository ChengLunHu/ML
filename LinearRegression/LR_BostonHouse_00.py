##########
# http://bigdataexaminer.com/uncategorized/how-to-run-linear-regression-in-python-scikit-learn/
##########

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

boston = datasets.load_boston()
boston.keys()
print boston.feature_names
