# # To add a new cell, type '# %%'
# # To add a new markdown cell, type '# %% [markdown]'
# # %%
# # Write a Python program to sort a list of elements using the quick sort algorithm.
# # Note : According to Wikipedia "Quicksort is a comparison sort, meaning that it can
# # sort items of any type for which a "less-than" relation (formally, a total order) is defined.
# # In efficient implementations it is not a stable sort, meaning that the relative order of equal
# # sort items is not preserved. Quicksort can operate in-place on an array, requiring small additional
# # amounts of memory to perform the sorting."
#
# ___ quickSort data_list
#    ? ? 0 le. ? -1
#
# ___ quickSortHlp data_list first last
#    __ ? < ?
#
#        splitpoint _ ? ? ? ?
#
#        ? ? ? ? - 1
#        ? ? ? + 1 ?
#
#
# ___ partition data_list first last
#    pivotvalue _ ? ?
#
#    leftmark _ ? + 1
#    rightmark _ ?
#
#    done _ F..
#    w___ no. ?
#
#        w___ l.. <_ r.. an. ? ? <_ p..
#            l.. _ ? + 1
#
#        w___ ? ? >_ p.. an. r.. >_ ?
#            r.. _ ? -1
#
#        __ r.. < ?
#            done _ T..
#        ____
#            temp _ ? l..
#            ? ? _ ? r..
#            ? ? _ ?
#
#    temp _ ? f..
#    ? ? _ ? r..
#    ? ? _ ?
#
#
#    r_ ?
#
# data_list _ [54,26,93,17,77,31,44,55,20]
# ? ?
# print(?)
#
#
