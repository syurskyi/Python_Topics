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
    sublistcount _ le.(alist)//2
    w___ sublistcount > 0:
      ___ start_position __ ra..(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)

      print("After increments of size",sublistcount, "The list is",nlist)

      sublistcount _ sublistcount // 2

___ gap_InsertionSort(nlist,start,gap):
    ___ i __ ra..(start+gap,le.(nlist),gap):

        current_value _ nlist[i]
        position _ i

        w___ position>_gap an. nlist[position-gap]>current_value:
            nlist[position]_nlist[position-gap]
            position _ position-gap

        nlist[position]_current_value


nlist _ [14,46,43,27,57,41,45,21,70]
shellSort(nlist)
print(nlist)


