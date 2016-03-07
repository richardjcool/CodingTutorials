# Pandas cheatsheet
import numpy as np
import pandas as pd

# Create a list of dates
dates = pd.date_range('20130101', periods=6)

# Create a dataframe with some random values
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# Getting values:
prices = df['prices']

# Return a subset of rows:
# Returns the first three rows of the table
df[0:3]

# Returns the rows with 0th column between two values
df['20130102':'20130104']

# Returns the types for each column
df.dtypes

# Returns an array of column names
df.columns

# Returns a matrix of the values in the table
df.values

# Sort by an axis (i.e. order the column names)
df.sort_index(axis=1, ascending=False)

# Sorting by values in a column
df.sort_values(by='C')

# Getting a cross section of a frame using a label
df.loc[dates[0]]   # Dates was defined above

# Selecting on a multi-axis by label
df.loc[:, ['A', 'B']]  # Give me all the data in A and B

# Select with label slicing (endpoints are *included*)
df.loc['20130102':'20130104', ['A','B']]

# Return a scalar value for a specific position
df.loc[dates[0], 'A']

# Select via the position of the pass integer
df.iloc[3]  # Returns the 3rd row

# Slicing with integers in both row and column
df.iloc[3:5, 0:2]  # Return 3, 4 rows with first two columns

# Or slice with lists of row/col
df.iloc[[1, 2, 4], [0, 2]]

# Return just the 2nd and 3rd row
df.iloc[1:3, :]

# Return 2nd and 3rd column
df.iloc[:, 1:3]

# Copying and adding a column
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

# Filter by "isin"
df2[df2['E'].isin(['two', 'four'])]  # If E is two or four, return that row

# You can apply a function to an array
df.apply(lambda x: x.max() - x.min())
df.apply(np.cumsum())
