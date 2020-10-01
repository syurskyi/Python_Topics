# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}                                                         
# Dictionary in ascending order by value :  [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]                            
# Dictionary in descending order by value :  [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]

______ operator

d _ {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d _ s..(d.i..(), key_operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d _ s..(d.i..(), key_operator.itemgetter(0),reverse_True)
print('Dictionary in descending order by value : ',sorted_d)


