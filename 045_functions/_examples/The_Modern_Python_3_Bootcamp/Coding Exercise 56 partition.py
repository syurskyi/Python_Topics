# Here's my solution that doesn't use a list comprehension:
#
#     I have two lists, to hold the true and false values
#     I loop through the list, calling fn  with each value in the list
#     If the result is True, I append the value to the trues  list
#     Otherwise, I append the value to the falses  list
#     At the end I return a list that contains both the trues  and falses  lists


def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]

# List Comprehension Version
#
# Using a list comprehension, you can get this function down to a single line.  It's definitely a tradeoff though.
# It's much short but also more difficult to understand.  It's a fine balance between brevity and readability.


def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]

# Another Solution
#
# This solution was submitted by a student named Jonathan.  Thanks, Jonathan!


def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)], l]
