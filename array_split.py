import numpy as np

# create the 4-deminsions matrx
arr1 = np.arange(1,17).reshape(4,4)

print(arr1)

# Another creating the 4 by 4 array of matrix 
arr2 = np.arange(17,33).reshape(4,4)

print(arr2)

# how to add the two list 

list1 = [1,2,3,4,5]

list2 = [6,7,8,9,10]

list3 = list1 + list2

print(list3)


# how to conctination the two matrix 

conctin_arr = np.concatenate((arr1,arr2))

print(conctin_arr)

# how to conctination the row and column wise

conctin_arr = np.concatenate((arr1,arr2),axis=1)

print(conctin_arr)

conctin_arr = np.concatenate((arr1,arr2),axis=0)

print(conctin_arr)

# another method to conctinate the two matrix by using the vstack
# vstake are using the vertially join the two matrix
conctin_arr = np.vstack((arr1,arr2))

print(conctin_arr)

# another method to conctinate the two matrix by using the hstack
# hstake are using the horizontally join the two matrix
conctin_arr = np.hstack((arr1,arr2))

print(conctin_arr)



# how to split the single array of matrix to multi array matrix by using split
conctin_arr = np.split(arr1 ,2,axis=1)

print(conctin_arr)

