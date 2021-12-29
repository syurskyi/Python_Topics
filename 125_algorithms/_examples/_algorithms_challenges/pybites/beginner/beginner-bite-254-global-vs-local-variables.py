"""
This Bite is to illustrate scoping. You will sum numbers while keeping track of number of
hundreds in a global variable called num_hundreds.

To illustrate this see this REPL output:

>>> from scoping import sum_numbers, num_hundreds
>>> num_hundreds
-1
>>> sum_numbers([10, 20, 70])
100
>>> from scoping import num_hundreds
>>> num_hundreds
0
>>> sum_numbers([10, 120, 180])
310
>>> from scoping import num_hundreds
>>> num_hundreds
3
We planned to also illustrate nonlocal, but we will do that in a separate Bite ...
Good luck and keep calm and code in Python!

"""

num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    list_sum = 0
    for n in numbers:
        list_sum += n
    how_many = int(list_sum/100)
    num_hundreds += how_many
    return list_sum

print(num_hundreds)
sum_numbers([10,20,70])
print(num_hundreds)
sum_numbers([10, 120, 180])

print(num_hundreds)