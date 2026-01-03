import numpy as np

# creating the 3 by 3 matrix not manually creating using the methods 
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(1,10).reshape(3,3)
print(arr1)
print(arr2)

# Adding the two matrix in onces 
sum_arr12 = arr1 + arr2
print(sum_arr12)

sum_arr12 = np.add(arr1,arr2)
print(sum_arr12)

# subtract the two matrix in onces 
sub_arr12 = arr1 - arr2
print(sub_arr12)

sub_arr12 = np.subtract(arr1 ,arr2)
print(sub_arr12)


# multiply the two matrix in onces 
sub_arr12 = arr1 * arr2
print(sub_arr12)

sub_arr12 = np.multiply(arr1 ,arr2)
print(sub_arr12)


# divide the two matrix in onces 
sub_arr12 = arr1/arr2
print(sub_arr12)

sub_arr12 = np.divide(arr1 ,arr2)
print(sub_arr12)


# if we want to multply the first row first column then we used the @
sub_arr12 = arr1 @ arr2
print(sub_arr12)

sub_arr12 = arr1.dot(arr2)
print(sub_arr12)

# How to find the MAX() value in any array
max_value = arr1.max()
print(max_value)

# How to find the index of MAX() value in any array
max_value = arr1.argmax()
print(max_value)

# How to find the MAX() value in column
max_value = arr1.max(axis=0)
print(max_value)

# How to find the MAX() value in row
max_value = arr1.max(axis=1)
print(max_value)


# How to find the MIN() value in array
max_value = arr1.min()
print(max_value)

# How to find the index of MIN() value in array
max_value = arr1.argmin()
print(max_value)


# How to find the MIN() value in array row
max_value = arr1.min(axis=1)
print(max_value)


# How to find the MIN() value in array column
max_value = arr1.min(axis=0)
print(max_value)
