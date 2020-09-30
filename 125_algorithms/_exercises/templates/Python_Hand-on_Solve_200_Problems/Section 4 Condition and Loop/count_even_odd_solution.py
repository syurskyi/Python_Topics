# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5

numbers _ (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd _ 0
count_even _ 0
___ x __ numbers:
        __ no. x % 2:
    	     count_even+_1
        ____
    	     count_odd+_1
                
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


