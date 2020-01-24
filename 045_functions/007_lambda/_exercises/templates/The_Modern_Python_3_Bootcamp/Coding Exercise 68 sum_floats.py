# Sum Floats Solution
#
# Write a function called sum_floats. This function should accept a variable number of arguments.
# The function should return the sum of all the parameters that are floats.
# If there are no floats the function should return 0
#
#     I started by defining sum_floats , which accepts any number of arguments using *args
#     Much like the previous exercise,
#     I use a generator expression to extract the values in args where type()  is float.
#     I pass those values in to sum  and return the result


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float)
