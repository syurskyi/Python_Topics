# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to sort a list of elements using the quick sort algorithm.
# Note : According to Wikipedia "Quicksort is a comparison sort, meaning that it can 
# sort items of any type for which a "less-than" relation (formally, a total order) is defined. 
# In efficient implementations it is not a stable sort, meaning that the relative order of equal 
# sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional
# amounts of memory to perform the sorting."

___ quickSort(data_list):
   quickSortHlp(data_list,0,le.(data_list)-1)

___ quickSortHlp(data_list,first,last):
   __ first < last:

       splitpoint _ partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


___ partition(data_list,first,last):
   pivotvalue _ data_list[first]

   leftmark _ first+1
   rightmark _ last

   done _ F..
   w___ no. done:

       w___ leftmark <_ rightmark an. data_list[leftmark] <_ pivotvalue:
           leftmark _ leftmark + 1

       w___ data_list[rightmark] >_ pivotvalue an. rightmark >_ leftmark:
           rightmark _ rightmark -1

       __ rightmark < leftmark:
           done _ T..
       ____
           temp _ data_list[leftmark]
           data_list[leftmark] _ data_list[rightmark]
           data_list[rightmark] _ temp

   temp _ data_list[first]
   data_list[first] _ data_list[rightmark]
   data_list[rightmark] _ temp


   r_ rightmark

data_list _ [54,26,93,17,77,31,44,55,20]
quickSort(data_list)
print(data_list)


