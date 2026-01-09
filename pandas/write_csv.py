# %%

import pandas as pd

# Using for the display data in. table view
from IPython.display import display
# Import the csv file
df = pd.read_csv('~/Downloads/customers-100.csv')
display(df)
df.columns
# Print  specific Row
df = pd.read_csv('~/Downloads/customers-100.csv',  nrows= 1)
display(df)

# Print  specific Column
df = pd.read_csv('~/Downloads/customers-100.csv',  usecols = [2])
display(df)

# Print  specific Column
df = pd.read_csv('~/Downloads/customers-100.csv',  usecols = [0,1,2])
display(df)

# Skip specific row
df = pd.read_csv('~/Downloads/customers-100.csv',  skiprows=1)
display(df)

# Import the csv file
df = pd.read_csv('~/Downloads/customers-100.csv')
display(df)

# Specific Column as a Index Value
df = pd.read_csv('~/Downloads/customers-100.csv', index_col= 'Index')
display(df)

# %%
