# how many times each character occurred in a string:
text = 'Some long text'
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

# how many times each character occurred in a string:
#
# Suppose now that we just want a dictionary to track the uppercase, lowercase, and other characters in the string
# (i.e. kind of grouping the data by uppercase, lowercase, other) - again ignoring spaces:
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)

text = 'Some long text'

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        if key not in categories:
            categories[key] = set()  # set we'll insert the value into

        categories[key].add(c)
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

# how many times each character occurred in a string:
# We can simplify this a bit using setdefault:
text = 'Some long text'

categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

# how many times each character occurred in a string:
#
# Just to clean things up a but more, let's create a small utility function that will return the category key:
text = 'Some long text'

def cat_key(c):
    if c == ' ':
        return None
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_uppercase:
        return 'upper'
    else:
        return 'other'

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

# how many times each character occurred in a string:
#
# If you are not a fan of using if...elif... in the cat_key function we could do it this way as well
text = 'Some long text'

def cat_key(c):
    categories = {' ': None,
                 string.ascii_lowercase: 'lower',
                 string.ascii_uppercase: 'upper'}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return 'other'

cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' ')

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))