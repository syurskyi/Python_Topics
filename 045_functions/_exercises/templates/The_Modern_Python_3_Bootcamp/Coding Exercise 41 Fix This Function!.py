# Here's the initial broken state of the function:


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count

# To fix it, all we have to do is outdent the return statement
# so that it now only returns after the loop finishes running


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count