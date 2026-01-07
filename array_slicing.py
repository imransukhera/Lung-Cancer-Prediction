#%%

import numpy as np

# Creating the array of 100 element by 10=row and 10=column 2 dimensions array

arr_2d = np.arange(1,101).reshape(10,10)

print(arr_2d)

# How to find out the first index value

first_index = arr_2d[0,0]

print(first_index)

# How to find out the dimensions
find_dim = arr_2d[0,0].ndim

print(find_dim)

# How to print the first complete row
find_dim = arr_2d[0]

print(find_dim)

# How to print the first complete column to using slice method
find_dim = arr_2d[:,0]

print(find_dim)


# How to convert the single column to 2 dimensions 
find_dim = arr_2d[:,0:1]

print(find_dim)

# check the dimensions of this 
find_dim = arr_2d[:,0:1].ndim

print(find_dim)


# how to find out the specific colomn and row in the created function
find_dim = arr_2d[1:4,1:4]

print(find_dim)

# how to find out the all row and specific column
find_dim = arr_2d[:,1:4]

print(find_dim)

# how to find out the storage space 
print(arr_2d)
find_dim = arr_2d.itemsize

print(find_dim)

# how to find out the data type of the

find_dim = arr_2d.dtype

print(find_dim)


# %%
