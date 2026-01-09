#%%
import pandas as pd
import os

df = pd.read_csv('~/Downloads/customers-100.csv')

# display nicely in table format
from IPython.display import display
display(df)

# Check the Where is your data store
print(os.getcwd())

# %%
