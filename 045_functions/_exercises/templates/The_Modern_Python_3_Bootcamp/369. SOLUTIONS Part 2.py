# SOLUTIONS
# Part
# 2
# Solutions
# Part
# 2
#
# Titleize


def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


# find_factors


def find_factors(num):
    factors = []
    i = 1
    while (i <= num):
        if (num % i == 0):
            factors.append(i)
        i += 1
    return factors


# includes


def includes(item, val, start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]


# repeat


def repeat(string, num):
    if (num == 0):
        return ''
    i = 0
    newStr = ''
    while (i < num):
        newStr += string
        i += 1
    return newStr


# truncate


def truncate(string, n):
    if (n < 3):
        return "Truncation must be at least 3 characters."
    if (n > len(string) + 2):
        return string

    return string[:n - 3] + "..."