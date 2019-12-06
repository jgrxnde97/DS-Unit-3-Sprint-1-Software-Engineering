""" lambdata_jgrxnde9701 - a collection of data science helper functions """

# codes
import numpy as np
import pandas as pd
from scipy import stats

# datasets
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))


# functions
class CleanData:
    """
    a function that will clean your dataset
    """
    def __init__(self, df):
        self.df = df
    """
    will return the total number of null values, if any exists in dataset
    """
    def check_nulls(self):
        result = self.df.isnull().sum().sum()
        return result

    """
    takes array of data as an input then outputs integer labels
    that correspond with proportional bin rank
    """

    def ran_bag(self, data, segments=10):
        edge = segments + 1
        labels = range(1, edge, 1)
        return pd.qcut(data, q=segments, labels=labels)
