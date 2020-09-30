# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to convert an integer to a roman numeral.

c_ py_solution:
    ___ int_to_Roman(self, num):
        val _ [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb _ [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num _ ''
        i _ 0
        while  num > 0:
            ___ _ __ ra..(num // val[i]):
                roman_num +_ syb[i]
                num -_ val[i]
            i +_ 1
        r_ roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(4000))


