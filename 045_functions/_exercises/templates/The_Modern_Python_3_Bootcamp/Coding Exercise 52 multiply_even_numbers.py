# SOLUTION
#
#     In my solution, I start with a variable called total.
#     Since we're working with multiplication, I start it off as 1.
#     Then I iterate through the list, checking if each num is cleanly divisible by 2
#     If it is, I multiply total by the number
#     At the end, after the loop finishes, I return total


def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total
