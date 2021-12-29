from collections import namedtuple

"""
First idea was to go through the list and build a dictionary holding:
key: word
value: tuple(index, count)

and then make a run through this dictionary and build output list taking out indexes of words with count > 1.

But, I completely forgot that ** TUPLES ARE IMMUTABLE **. So I cannot update a tuple after it's created (cannot update counts).

So, quick fix for that was to replace namedtuple with dictionary. 
That worked, but I got puzzled by following construct:

Assuming dictionary like this:

{'is': {'index': 0, 'count': 2}, 'it': {'index': 1, 'count': 2}, 'true': {'index': 2, 'count': 1}, 'or': {'index': 3, 'count': 1}, 'not?': {'index': 6, 'count': 1}}

With following code:

for k, v in stats.values():
   print(k)
   print(v)

I get:

index
count
index
count
index
count
index
count
index
count

KEY TAKEAWAYS:

1. Checking for existence of key in dictionary

mydict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
}

key="one"

if key in mydict:
    print("Key exists") 
else:
    print("Key does not exist")

2. Tuples are immutable

3. It's easy to count particular item in a list:

words = ['is', 'on', 'the', 'way', 'way']

words.count('way')

4. It's easy to check index of a particular item in a list:

words.index('way') 

5. Once again, list comprehensions! But watch out! whether to use {} or []

duplicate_words = {word for word in words if words.count(word) > 1}
result = sorted([words.index(word) for word in duplicate_words]) 

6. dict, defaultdict, ordereddict, get method, exceptions

"""

def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first occurrence.
       For example in the following list 'is' and 'it'
       occur more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    stats = {}
    index = 0
    # Tuples are immutable!!!
    # MyPair = namedtuple('MyPair', 'index count')
    result = []
    for word in words:
        try:
            mp = stats[word]
            mp['count'] += 1
        except KeyError:
            mp = dict()
            mp['index'] = index
            mp['count'] = 1
            stats[word] = mp
        index += 1
    print(stats)
    for k, v in stats.values():
        print(k)
        print(v)

#    for k, v in stats.items():
#        if v['count'] > 1:
#            result.append(v['index'])

    print(result)
    return(result)


print(get_duplicate_indices(['is', 'it', 'true', 'or', 'is', 'it', 'not?']))