# %%
import numpy as np

# creating the two string array

ch_name = 'Muhammad Imran'
str1 = "Learn python"

# add the two string

np.char.add(ch_name, str1)

# string convert into lowercase

np.char.lower(ch_name)

# string convert into upper

np.char.upper(ch_name)

# Align the string into center 60 basically give the legnth
np.char.center(ch_name,60)

# fill the given white space with spcific charcter
np.char.center(ch_name,60, fillchar='*')

# split the string into single word
np.char.split(ch_name)
# %%
