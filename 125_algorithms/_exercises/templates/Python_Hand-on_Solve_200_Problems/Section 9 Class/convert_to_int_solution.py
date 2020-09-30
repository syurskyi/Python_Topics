# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python class to convert a roman numeral to an integer

# Sample input
# 'MMMCMLXXXVI'
# 'MMMM'
# 'C'

# Sample output
# 3986                                                                                                          
# 4000                                                                                                          
# 100

c_ py_solution:
    ___ roman_to_int(self, s):
        rom_val _ {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val _ 0
        ___ i __ ra..(le.(s)):
            __ i > 0 an. rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val +_ rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            ____
                int_val +_ rom_val[s[i]]
        r_ int_val

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))


