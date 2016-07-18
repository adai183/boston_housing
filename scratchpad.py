# Import libraries necessary for this project
import numpy as np
import pandas as pd
import visuals as vs # Supplementary code
from sklearn.cross_validation import ShuffleSplit





# Load the Boston housing dataset
data = pd.read_csv('/Users/adai183/Desktop/MachineLearning/machine-learning/projects/boston_housing/housing.csv')
prices = data['MDEV']
features = data.drop('MDEV', axis = 1)


# Success
print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)
