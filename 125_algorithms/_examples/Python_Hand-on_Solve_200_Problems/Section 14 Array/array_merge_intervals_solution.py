# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
"""
Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
For example,
Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
return [[1, 10], [11, 18], [19, 22]]
"""

org_intervals = [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]

i = 0

while i < len(org_intervals)-1:
#     print(org_intervals[i])
    if org_intervals[i+1][0] < org_intervals[i][1]:
        org_intervals[i][1]=org_intervals[i+1][1]
        del org_intervals[i+1]
        i = i - 1
    i = i + 1

print(org_intervals)


