# SOLUTIONS Part 1
# Solutions Part 1
#
# reverse_string

def reverse_string(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s

# list_check

def list_check(vals):
    return all(type(l) == list for l in vals)

# remove_every_other

def remove_every_other(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]

# sum_pairs

def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []

# vowel_count

def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}