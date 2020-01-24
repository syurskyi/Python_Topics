# decrement_list solution
#
#     I define the function decrement_list that accepts a list called l
#     Inside, I call map and pass in a lambda and the list, l
#         The lambda returns n-1 for each n in the list
#     The last step is to convert the return value of map to a list
#         Remember, map returns a <map object>, not a list
#     Oh, and finally we return the result!


def decrement_list(l):
    return list(map(lambda n: n - 1, l))
