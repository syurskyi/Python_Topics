# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#  Write a Python program to convert Year/Month/Day to Day of Year in Python
______ datetime
today _ datetime.datetime.now()
day_of_year _ (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)


