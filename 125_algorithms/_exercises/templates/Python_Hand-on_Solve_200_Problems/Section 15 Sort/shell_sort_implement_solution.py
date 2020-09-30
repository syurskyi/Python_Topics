# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to sort a list of elements using shell sort algorithm.
# Note : According to Wikipedia "Shell sort or Shell's method, is an in-place comparison sort. 
# It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort). 
# The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between
# elements to be compared. Starting with far apart elements can move some out-of-place elements into position faster than
# a simple nearest neighbor exchange."


# %%
___ shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      ___ start_position __ ra..(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)

      print("After increments of size",sublistcount, "The list is",nlist)

      sublistcount = sublistcount // 2

___ gap_InsertionSort(nlist,start,gap):
    ___ i __ ra..(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value


nlist = [14,46,43,27,57,41,45,21,70]
shellSort(nlist)
print(nlist)


