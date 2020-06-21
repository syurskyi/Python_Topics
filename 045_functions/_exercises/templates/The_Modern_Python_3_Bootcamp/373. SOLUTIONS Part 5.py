# Solutions
# Part
# 5
#
# valid_parentheses


def valid_parentheses(parens):
    count = 0
    i = 0
    while i < len(parens):
        if (parens[i] == '('):
            count += 1
        if (parens[i] == ')'):
            count -= 1
        if (count < 0):
            return False
        i += 1
    return count == 0


# reverse_vowels


def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)


# three_odd_numbers


def three_odd_numbers(arr):
    i = 0
    while (i < (len(arr) - 2)):
        total = 0
        j = i
        while (j <= i + 2):
            total += arr[j]
            j += 1

        if (j - i) % 3 == 0 and total % 2 != 0:
            return True

        i += 1
    return False


# mode


def mode(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]


# running_average


def running_average():
    running_average.accumulator = 0
    running_average.size = 0

    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size

    return inner