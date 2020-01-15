""" lambdata_jgrxnde9701 - a collection of data science helper functions """

# codes
import numpy as np
import pandas as pd
from scipy import stats


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
    removes rows that have at least one value that
    is n-standard deviations from a column mean
    """

    def outlier_filter(self, deviations=2):
        return self.df[(np.abs(stats.zscore(
            self.df)) < deviations).all(axis=1)]

    """
    takes array of data as an input then outputs integer labels
    that correspond with the proportional bin rank
    """

    def ran_bag(self, data, segments=10):
        edge = segments + 1
        labels = range(1, edge, 1)
        return pd.qcut(data, q=segments, labels=labels)
