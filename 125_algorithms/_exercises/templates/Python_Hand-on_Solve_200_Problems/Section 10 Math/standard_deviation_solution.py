# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to calculate the standard deviation of the following data.
# Input
# Sample Data:  [4, 2, 5, 8, 6]                                                                                 
# Output
# Standard Deviation :  2.23606797749979

import math
import sys

___ sd_calc(data):
    n = len(data)

    if n <= 1:
        r_ 0.0

    mean, sd = avg_calc(data), 0.0

    # calculate stan. dev.
    ___ el __ data:
        sd += (float(el) - mean)**2
    sd = math.sqrt(sd / float(n-1))

    r_ sd


___ avg_calc(ls):
    n, mean = len(ls), 0.0

    if n <= 1:
        r_ ls[0]

    # calculate average
    ___ el __ ls:
        mean = mean + float(el)
    mean = mean / float(n)

    r_ mean

data = [4, 2, 5, 8, 6]
print("Sample Data: ",data)
print("Standard Deviation : ",sd_calc(data))


