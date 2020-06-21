print('#' * 52 + ' ### Common Operations  ')

d = dict(zip('abc', range(1, 4)))
print(d)
print(len(d))
print(d['a'])
# print(d['python']) # KeyError: 'python'

print('#' * 52 + ' Sometimes though, we do not want an exception to happen, and we want to provide some default'
                 ' value instead. We could certainly catch the exception, but thats clunky. Instead we can use the'
                 ' `get` instance method: ')

d.get('a')
result = d.get('python')
print(result)

print('#' * 52 + ' As you can see, we do not get an exception, we simply get `None` back. We can actually specify '
                 ' the default to use when the key is not found: ')

print(d.get('python', 0))

print('#' * 52 + ' count letters ')

text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam' \
       ' rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, ' \
       'explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur' \
       ' magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum,' \
       ' quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt,' \
       ' ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem' \
       ' ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure' \
       ' reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem' \
       ' eum fugiat, quo voluptas nulla pariatur?'
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)

print('#' * 52 + ' We can refine this a bit - first we ll ignore spaces, then we ll want to consider lowercase and '
                 ' uppercase characters as the same:  ')

counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)

print('#' * 52 + ' #### Membership Tests  ')
print('#' * 52 + ' We can use the `in` and `not in` operators to test the presence of a **key** in a dictionary:  ')

d = dict(a=1, b=2, c=3)
print('a' in d)
print('z' in d)
print('z' not in d)

print('#' * 52 + ' #### Removing elements from a dictionary  ')

d = dict.fromkeys('abcd', 0)
print(d)

print('#' * 52 + ' We can remove a key this way:  ')

del d['a']
print(d)

print('#' * 52 + ' If the key is not present, we will get a `KeyError` exception: ')

# del d['z'] KeyError: 'z'

result = d.pop('b')
print(result)

print('#' * 52 + ' So we still get a `KeyError` exception! To do this, we need to specify a **default** value'
                 ' to use if the key is not found: ')

result = d.pop('z', 'Not found!')
print(result)

print('#' * 52 + '  ')

d = {'a': 10, 'b': 20, 'c': 30}
print(d.popitem())
print(d.popitem())
print(d.popitem())
# print(d.popitem()) #  KeyError: 'popitem(): dictionary is empty'

print('#' * 52 + ' #### Inserting keys with a default  ')
d = {'a': 1, 'b': 2, 'c': 3}
if 'z' not in d:
    d['z'] = 0

print(d)

print('#' * 52 + ' We could write a simple utility function to do this for us, and return the value of the item as well'
                 ' while were at it: ')

def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]

print(d)
result = insert_if_not_present(d, 'a', 0)
print(result, d)

result = insert_if_not_present(d, 'y', 10)
print(result, d)

print('#' * 52 + ' But instead, we can simply use the `setdefault` instance method, which will do the work we just did')

d = {'a': 1, 'b': 2, 'c': 3}
result = d.setdefault('a', 0)
print(result)
print(d)

result = d.setdefault('z', 100)
print(result)
print(d)

print('#' * 52 + '  ')

text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem' \
       ' aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo.' \
       ' Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni' \
       ' dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor' \
       ' sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore' \
       ' et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam' \
       ' corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure' \
       ' reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum,' \
       'qui dolorem eum fugiat, quo voluptas nulla pariatur?'
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)

print('#' * 52 + ' Heres one approach we might take:  ')

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

print('#' * 52 + '  We can simplify this a bit using `setdefault`: ')

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


print('#' * 52 + '  Just to clean things up a but more, lets create a small utility function that will return'
                 ' the category key: ')

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


print('#' * 52 + ' If you are not a fan of using `if...elif...` in the `cat_key` function we could do it this way'
                 ' as well: ')

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

print('#' * 52 + ' This approach is easier to extend without having a lot of `elif` statements,'
                 ' but for a few categories, I find the first implementation much clearer to read and understand. ')

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))


print('#' * 52 + ' We could also do it this way, creating a categories dictionary that has all the individual'
                 ' characters we are interested in:  ')

from itertools import chain

def cat_key(c):
    cat_1 = {' ': None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')
    categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
    # categories = {**cat_1, **cat_2, **cat_3} - I'll explain this later
    return categories.get(c, 'other')

cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' ')

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))

print('#' * 52 + '  #### Clearing All Items ')
print('#' * 52 + ' If we want to remove all the keys in a dictionary, we can use the `clear` method: ')

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
d.clear()
print(d)
