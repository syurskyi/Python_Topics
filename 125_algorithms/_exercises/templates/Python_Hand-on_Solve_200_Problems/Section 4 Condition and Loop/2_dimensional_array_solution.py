# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.

# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  

# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 ___ col __ ra..(col_num)] ___ row __ ra..(row_num)]

___ row __ ra..(row_num):
    ___ col __ ra..(col_num):
        multi_list[row][col]= row*col

print(multi_list)

