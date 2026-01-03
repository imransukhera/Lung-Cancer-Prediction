import numpy as np

# Arange Fuction
# Syntx of the arange function is 

# np.arange(star,end,steps)
ar_1d = np.arange(1,13)
print(ar_1d)

# If we want to seperate the even number in this array
even_1d = np.arange(1,13,2)
print(even_1d)

# If we want to seperate the odd number inside it 
od_1d = np.arange(1,13,3)
print(od_1d)

# If we create the array within number 
ls_1d = np.linspace(1,5,4)
print(ls_1d)

# its used to create the single dimensions array to multi-dimensions array
ar_2d = ar_1d.reshape(3,4)
print(ar_2d)

# its used to create the multi-dimensions dimensions array to single dimensions  array
single_1d = ar_2d.ravel()
print(single_1d)

# its used to create the multi-dimensions dimensions array to single dimensions  array
fM_1d = ar_2d.flatten()
print(fM_1d)

# its used to create the multi-dimensions dimensions 
transpose_1d = ar_2d.transpose()
print(transpose_1d)
