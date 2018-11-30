import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
s


dates = pd.date_range('20130101', periods = 5)
dates
type(dates)

df = pd.DataFrame(np.random.randn(5,4), index = dates, columns=list('ABCD'))
df
np.random.randint(5,20,size=[5, 6])

df2 = pd.DataFrame({'A': 1.,
                 'B': pd.Timestamp('20130102'),
                 'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                 'D': np.array([3]*4, dtype='int32'),
                 'E': pd.Categorical(["test", "train", "test", "train"]),
                 'F': 'foo'})
df2
pd.Timestamp('20130102')
pd.Series(1, index=list(range(4)), dtype='float32')
np.array([3]*4, dtype='int32')
pd.Categorical(["test", "train", "test", "train"])
df2.dtypes
df2

df.index
df.columns
df.values

df.describe()
df.T
df.sort_index(axis = 1, ascending = False)
df.sort_values(by='B')