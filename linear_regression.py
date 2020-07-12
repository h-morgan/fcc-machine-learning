from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc
import tensorflow as tf

# training dataset
dftrain = pd.read_csv("data/titanic-train.csv")
# testing dataset
dfeval = pd.read_csv("data/titanic-eval.csv")

# remove and returns the column of data that we are trying to ultimately predict
y_train = dftrain.pop("survived")
y_eval = dfeval.pop("survived")

# Just exploring dataframe a bit -- print any of these variables to review outputs
# This looks at the first row in both dftrain and y_trainl
first_row_dftrain = dftrain.loc[0]
first_row_y_train = y_eval.loc[0]
# This looks at the age column in the df
age_column = dftrain['age']

# Describe dataset -- a statistics overview of the data 
describe = dftrain.describe()
shape = dftrain.shape # 627 rows, 9 columns



