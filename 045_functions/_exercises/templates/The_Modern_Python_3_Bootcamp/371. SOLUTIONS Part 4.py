# Solutions
# Part
# 4
#
# sum_up_diagonals


def sum_up_diagonals(arr):
    total = 0

    for i, val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1 - i]
    return total


# min_max_key_in_dictionary


def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]


# find_greater_numbers


def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j += 1
        j = i + 1
        i += 1
    return count;


# two_oldest


def two_oldest_ages(ages):
    return sorted(ages)[-2:]


# is_odd_string


def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1