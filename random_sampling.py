# %%
import numpy as np
import random

# Creating the random value
np.random.random(1)

# creating the 2d array by using the random method
np.random.random((3,3))

# Creating the integrate type value by using the random method
np.random.randint(1,3)

# creating 2d array assign the range and which type of matrix you want 
np.random.randint(1,4,(4,4))

# create the two time 2d matrix by using randInt method
np.random.randint(1,4,(2,4,4))

# seed method are used to create the same matrix everytime
np.random.seed(10)
np.random.randint(1,4,(2,4,4))

# seed method are used to create the same matrix everytime
np.random.seed(10)
np.random.randint(1,4,(2,4,4))

# how much numbers os seed 
# We have 2**32 - 1 range of seed numbers means total numbers is 4294967295
2**32 - 1 

# randn method are used to create the nagtive and postive value
np.random.randn(3,3)

# using the choise method to select the one element in the array
x = [1,2,3,4,5]
np.random.choice(x)

# Using for loop to print the choise method
for i in range(20):
    print(np.random.choice(x))
# %%
