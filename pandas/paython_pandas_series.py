#%%
# Import thepandas
import pandas as pd

# Check the version of pandas
pd.__version__
print(pd.__version__)

# Create the list of value
list_s = [1,2,-3,6.2,'Data Vallue']
print(list_s)

# create the pandas series by using the list
series1 = pd.Series(list_s)
print(series1)
# Check the data Type
type(series1)

# Create the directly series
series2 = pd.Series([1,2,3,4])
print(series2)

# Create a empty series
empty_s = pd.Series([])
print(empty_s)

# Assign the index value
series3 = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(series3)

# Assign the index value
series4 = pd.Series([1,2,3,4], index=['a','b','c','d'], dtype= float)
print(series4)

# Assign the index value
series5 = pd.Series([1,2,3,4], index=['a','b','c','d'], dtype= float, name='data vallues')
print(series5)


# Assign the index value
scaler_s = pd.Series([0.5])
print(scaler_s)

# Assign the index value
dynamic_servie = pd.Series(0.5, index=[1,2,3,4])
print(dynamic_servie)

# Create the series with the help of dictionary
dict_s = pd.Series({'a':1, 'b':2, 'c':4})
print(dict_s)

# Access the the index of value 
s4 = series2[0]
print(s4)

# How to get the specific value means slice
s5 = series2[0:3]
print(s5)

# How to get the Maximum value
max5 = max(series2)
print(max5)



# %%
