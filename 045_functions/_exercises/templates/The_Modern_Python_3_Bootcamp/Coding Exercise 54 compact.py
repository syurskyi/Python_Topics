# With a list comprehension
#
# You can write compact  in a nice single line of code.  How compact!


def compact(l):
    return [val for val in l if val]

# Without a list comprehension
#
#     I make a list to store all truthy values
#     I iterate over each value in the list
#     I check if the value is truthy (using a simple if val )
#         If the value is truthy, add it to the truthy_vals  list
#     return truthy_vals  at the end


def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals
