# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 
# These brackets must be close in the correct order, 
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

c_ py_solution:
   ___ is_valid_parenthese(self, str1):
        stack, pchar _   # list, {"(": ")", "{": "}", "[": "]"}
        ___ parenthese __ str1:
            __ parenthese __ pchar:
                stack.ap..(parenthese)
            elif le.(stack) __ 0 or pchar[stack.p..()] !_ parenthese:
                r_ F..
        r_ le.(stack) __ 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))


