# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to sort a list of elements using the selection sort algorithm.
# Note : The selection sort improves on the bubble sort by making only one exchange for every pass through the list.

# %% [markdown]
# ![selection-short.png](attachment:selection-short.png)

# %%
___ selectionSort(nlist):
   ___ fillslot __ ra..(le.(nlist)-1,0,-1):
       maxpos_0
       ___ location __ ra..(1,fillslot+1):
           __ nlist[location]>nlist[maxpos]:
               maxpos _ location

       temp _ nlist[fillslot]
       nlist[fillslot] _ nlist[maxpos]
       nlist[maxpos] _ temp

nlist _ [14,46,43,27,57,41,45,21,70]
selectionSort(nlist)
print(nlist)


