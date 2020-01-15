"""
lambdata_jgrxnde9701 - utility functions for working with DataFrames
"""

# codes
import pandas as pd
import numpy as np

# dataframes
df_null = pd.DataFrame([2, 2, 3, 5, np.NaN, 7, 8, 9, 9, np.NaN])

df_ran = pd.DataFrame(np.random.randn(200, 5))

df_test = pd.DataFrame([1, 2, 4, 4, 6, 7, 8, 0])

df_ran_column = df_ran[0]
