# %%
# Import pandas 
import pandas as pd

# How to create python dataframe
empty_df = pd.DataFrame([])
print(empty_df)

list_s = ['a','b','c']
print(list_s)

# Create the dataframe by using list
df_1 = pd.DataFrame(list_s)
print(df_1)

list_list = [[1,2,3],[2,3,4],[3,4,5]]
print(list_list)

df_2 = pd.DataFrame(list_list)
print(df_2)
# %%
