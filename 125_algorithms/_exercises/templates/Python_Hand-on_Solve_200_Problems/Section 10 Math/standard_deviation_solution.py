# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to calculate the standard deviation of the following data.
# Input
# Sample Data:  [4, 2, 5, 8, 6]                                                                                 
# Output
# Standard Deviation :  2.23606797749979

______ math
______ sys

___ sd_calc(data):
    n _ le.(data)

    __ n <_ 1:
        r_ 0.0

    mean, sd _ avg_calc(data), 0.0

    # calculate stan. dev.
    ___ el __ data:
        sd +_ (fl..(el) - mean)**2
    sd _ math.sqrt(sd / fl..(n-1))

    r_ sd


___ avg_calc(ls):
    n, mean _ le.(ls), 0.0

    __ n <_ 1:
        r_ ls[0]

    # calculate average
    ___ el __ ls:
        mean _ mean + fl..(el)
    mean _ mean / fl..(n)

    r_ mean

data _ [4, 2, 5, 8, 6]
print("Sample Data: ",data)
print("Standard Deviation : ",sd_calc(data))


