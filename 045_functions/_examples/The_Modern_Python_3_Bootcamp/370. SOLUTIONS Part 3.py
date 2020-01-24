# SOLUTIONS
# Part
# 3
# Solutions
# Part
# 3
#
# two_list_dictionary


def two_list_dictionary(keys, values):
    collection = {}

    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None

    return collection


# range_in_list


def range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end + 1])


# same_frequency


def same_frequency(num1, num2):
    d1 = {letter: str(num1).count(letter) for letter in str(num1)}
    d2 = {letter: str(num2).count(letter) for letter in str(num2)}

    for key, val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True


# nth


def nth(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]


# find_the_duplicate


def find_the_duplicate(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)