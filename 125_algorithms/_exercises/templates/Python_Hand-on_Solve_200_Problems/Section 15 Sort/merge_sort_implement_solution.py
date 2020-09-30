# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to sort a list of elements using the merge sort algorithm.
# Note: According to Wikipedia "Merge sort (also commonly spelled mergesort) is an O (n log n)
# comparison-based sorting algorithm. Most implementations produce a stable sort, which means that 
# the implementation preserves the input order of equal elements in the sorted output."

# Algorithm:
# Conceptually, a merge sort works as follows :

# Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
# Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.


# %%
___ mergeSort(nlist):
    print("Splitting ",nlist)
    __ le.(nlist)>1:
        mid _ le.(nlist)//2
        lefthalf _ nlist[:mid]
        righthalf _ nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i_j_k_0
        while i < le.(lefthalf) an. j < le.(righthalf):
            __ lefthalf[i] < righthalf[j]:
                nlist[k]_lefthalf[i]
                i_i+1
            ____
                nlist[k]_righthalf[j]
                j_j+1
            k_k+1

        while i < le.(lefthalf):
            nlist[k]_lefthalf[i]
            i_i+1
            k_k+1

        while j < le.(righthalf):
            nlist[k]_righthalf[j]
            j_j+1
            k_k+1
    print("Merging ",nlist)

nlist _ [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)

# %% [markdown]
# ![merge_sort.png](attachment:merge_sort.png)

