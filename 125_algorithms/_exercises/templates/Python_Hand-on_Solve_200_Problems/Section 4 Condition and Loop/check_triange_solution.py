# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to check a triangle is valid or not

___ triangle_check(l1,l2,l3):
    __ (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('No, the lengths wont form a triangle')
    ____ (l1__l2+l3) or (l2__l1+l3) or (l3__l1+l2):
        print('yes, it can form a degenerated triangle')
    ____
        print('Yes, a triangle can be formed out of it')

length1 _ in.(i..('enter side 1\n'))
length2 _ in.(i..('enter side 2\n'))
length3 _ in.(i..('enter side 3\n'))

triangle_check(length1,length2,length3)

