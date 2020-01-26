# # %%
# '''
# # Dynamic Array Exercise
# ____
# 
# In this exercise we will create our own Dynamic Array class!
# We'll be using a built in library called [ctypes](https://docs.python.org/2/library/ctypes.html).
# Check out the documentation for more info, but its basically going to be used here as a raw array from
# the ctypes module.
# If you find yourself very interested in it, check out:
# [Ctypes Tutorial](http://starship.python.net/crew/theller/ctypes/tutorial.html)
# 
# Also...
# '''
# 
# # %%
# '''
# **A quick note on public vs private methods, we can use an underscore _ before the method name to keep it non-public. 
# For example:**
# '''
# 
# 
# # %%
# c_ M o..
# 
#     ___ public ____
#         print('Use Tab to see me!')
# 
#     ___ _private ____
#         print("You won't be able to Tab to see me!")
# 
# 
# # %%
# m = ?
# 
# # %%
# ?.p...
# 
# # %%
# ?._p..
# 
# print()
# print()
# # %%
# '''
# Check out PEP 8 and the Python docs for more info on this!
# _____
# 
# ### Dynamic Array Implementation
# '''
# 
# # %%
# _________ ct
# 
# 
# c_ DynamicArray o..
#     '''
#     DYNAMIC ARRAY CLASS (Similar to Python List)
#     '''
# 
#     ___ -  ____
#         ____.n _ 0  # Count actual elements (Default is 0)
#         ____.capacity _ 1  # Default Capacity
#         ____.A _ ____.make_array ____.c...
# 
#     ___ -  ____
#         """
#         Return number of elements sorted in array
#         """
#         r_ ____.n
# 
#     ___ -g  ____ k
#         """
#         Return element at index k
#         """
#         i_ no. 0 <_ k < ____.n
#             r_ _I...('K is out of bounds!')  # Check it k index is in bounds of array
# 
#         r_ ____.A k  # Retrieve from array at index k
# 
#     ___ append ____ ele
#         """
#         Add element to end of the array
#         """
#         i_ ____.n __ ____.c...
#             ____._res..(2 * ____.ca..  # Double capacity if not enough room
# 
#         ____.A ____.n _ e..  # Set ____.n index to element
#         ____.n +_ 1
# 
#     ___ _resize ____ new_cap
#         """
#         Resize internal array to capacity new_cap
#         """
# 
#         B = ____.make_array n..  # New bigger array
# 
#         ___ k i_ ra.. ____.n  # Reference all existing values
#             B k _ ____.A k
# 
#         ____.A _ B  # Call A the new bigger array
#         ____.c... = n...  # Reset the capacity
# 
#     ___ make_array ____ new_cap
#         """
#         Returns a new array with new_cap capacity
#         """
#         r_ n.. * ct___.py_object
# 
# 
# # %%
# # Instantiate
# arr = ?
# 
# # %%
# # Append new element
# ?.? 1
# 
# # %%
# # Check length
# print ? ?
# 
# # %%
# # Append new element
# ? ? 2
# 
# # %%
# # Check length
# print ? ?
# 
# # %%
# # Index
# print ? 0
# 
# # %%
# print ? 1
# 
# # %%
# '''
# Awesome, we made our own dynamic array! Play around with it and see how it auto-resizes. 
# Try using the same **sys.getsizeof()** function we worked with previously!
# '''
# 
# # %%
# '''
# # Great Job!
# '''
