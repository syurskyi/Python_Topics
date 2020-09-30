# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program for sequential search.
# Sequential Search: In computer science, linear search or sequential search is a method for finding a particular value in a list
# that checks each element in sequence until the desired element is found or the list is exhausted. The list need not be ordered.


___ Sequential_Search(dlist, item):

    pos _ 0
    found _ F..
    
    while pos < le.(dlist) an. no. found:
        __ dlist[pos] __ item:
            found _ T..
        ____
            pos _ pos + 1
    
    r_ found, pos

print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))


