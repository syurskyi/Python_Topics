# My solution works by:
#
#     Slicing the first character (up to index 1) and capitalizing it
#     Adding that to the rest of the string (from index 1 onward)


def capitalize(string):
    return string[:1].upper() + string[1:]