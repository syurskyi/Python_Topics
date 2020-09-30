# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to sort a list of elements using the insertion sort algorithm.
# Note: According to Wikipedia "Insertion sort is a simple sorting algorithm that builds 
# the final sorted array (or list) one item at a time. It is much less efficient on large
# lists than more advanced algorithms such as quicksort, heapsort, or merge sort."

# %% [markdown]
# ![insertion-sort.png](attachment:insertion-sort.png)

# %%
___ insertionSort(nlist):
   ___ index __ ra..(1,le.(nlist)):

     currentvalue _ nlist[index]
     position _ index

     while position>0 an. nlist[position-1]>currentvalue:
         nlist[position]_nlist[position-1]
         position _ position-1

     nlist[position]_currentvalue

nlist _ [14,46,43,27,57,41,45,21,70]
insertionSort(nlist)
print(nlist)


