# Import the Numpy library
import numpy as np

# Creating the 3 dimintional matrix 
mx_3d = np.array([[1,1,1],[1,1,1],[1,1,1]])
print(mx_3d)

# this command used to create the once row 
mx_1s = np.ones(5)
print(mx_1s)

# Check the Data tupe 
print(mx_1s.dtype)

# Create the 1 number matrix 3 row and 4 column
mx_1s = np.ones((3,4))
print(mx_1s)

# Assign the specific data type means 'INT'
mx_1s = np.ones((3,4), dtype=int)
print(mx_1s)

# Create the 0 matrix at once 4=rows and 6=column
mx_0s = np.zeros((4,6))
print(mx_0s)

# Assign the specific data type means 'INT'
mx_0s = np.zeros((4,6), dtype=int)
print(mx_0s)

# Assign the data type boolean
mx_0s = np.zeros((4,6), dtype=bool)
print(mx_0s)

# Assign the data type string
mx_0s = np.zeros((4,6), dtype=str)
print(mx_0s)

# Create the empty matrix
em_mx = np.empty((3,3))
print(em_mx)