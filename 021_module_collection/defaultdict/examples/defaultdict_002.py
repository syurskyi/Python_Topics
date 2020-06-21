from collections import defaultdict

# Let's take a look at another example of where a defaultdict can be useful.
# Suppose we have a dictionary structure that has people's names as keys, and a dictionary for the value that contains
# the person's eye color. We want to create a dictionary of eye colors, with a list of the people's names that have
# that eye color:

persons = {
    'john': {'age': 20, 'eye_color': 'blue'},
    'jack': {'age': 25, 'eye_color': 'brown'},
    'jill': {'age': 22, 'eye_color': 'blue'},
    'eric': {'age': 35},
    'michael': {'age': 27}
}

# What we want is a dictionary with the eye colors (and unknown as the key if the eye color was not specified),
# and the names of the people with that eye color.
# Let's first do this without a defaultdict, and also not using .get:

eye_colors = {}
for person, details in persons.items():
    if 'eye_color' in details:
        color = details['eye_color']
    else:
        color = 'unknown'
    if color in eye_colors:
        eye_colors[color].append(person)
    else:
        eye_colors[color] = [person]

print(eye_colors)
# {'blue': ['john', 'jill'], 'brown': ['jack'], 'unknown': ['eric', 'michael']}

# Now let's simplify this by leveraging the .get method:

eye_colors = {}
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    person_list = eye_colors.get(color, [])
    person_list.append(person)
    eye_colors[color] = person_list

print(eye_colors)
# {'blue': ['john', 'jill'], 'brown': ['jack'], 'Unknown': ['eric', 'michael']}

# And finally let's use a defaultdict:

eye_colors = defaultdict(list)

for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    eye_colors[color].append(person)

print(eye_colors)
# defaultdict(list,
#             {'blue': ['john', 'jill'],
#              'brown': ['jack'],
#              'Unknown': ['eric', 'michael']})

# When we create a defaultdict we have to specify the factory method as the first argument, but thereafter we can
# specify key/value pairs just like we would with the dict constructor (they are basically just passed along to the underlying dict):

d = defaultdict(bool, k1=True, k2=False, k3='python')
d
# defaultdict(bool, {'k1': True, 'k2': False, 'k3': 'python'})

# So, using this, if we had used a defaultdict for the Person values, we could simplify our previous example a bit more:

persons = {
    'john': defaultdict(lambda: 'unknown',
                        age=20, eye_color='blue'),
    'jack': defaultdict(lambda: 'unknown',
                        age=20, eye_color='brown'),
    'jill': defaultdict(lambda: 'unknown',
                        age=22, eye_color='blue'),
    'eric': defaultdict(lambda: 'unknown', age=35),
    'michael': defaultdict(lambda: 'unknown', age=27)
}

eye_colors = defaultdict(list)

for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)

print(eye_colors)

# defaultdict(list,
#             {'blue': ['john', 'jill'],
#              'brown': ['jack'],
#              'unknown': ['eric', 'michael']})

# It was a little tedious defining that defaultdict for every instance in our persons dictionary.
# This is a good example of where a partial function would be really useful. (I cover partial functions in Part
# 1 of this series, or you can review the documentation here:
# https://docs.python.org/3.7/library/functools.html#functools.partial
# (You can also just use a lambda function as well)

from functools import partial
eyedict = partial(defaultdict, lambda: 'unknown')

# Alternatively we could also just define it this way:

eyedict = lambda *args, **kwargs: defaultdict(lambda: 'unknown', *args, **kwargs)

persons = {
    'john': eyedict(age=20, eye_color='blue'),
    'jack': eyedict(age=20, eye_color='brown'),
    'jill': eyedict(age=22, eye_color='blue'),
    'eric': eyedict(age=35),
    'michael': eyedict(age=27)
}

print(persons)

# {'john': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
#              {'age': 20, 'eye_color': 'blue'}),
#  'jack': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
#              {'age': 20, 'eye_color': 'brown'}),
#  'jill': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
#              {'age': 22, 'eye_color': 'blue'}),
#  'eric': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
#              {'age': 35}),
#  'michael': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
#              {'age': 27})}

# And we can use our previous code just as before:

eye_colors = defaultdict(list)
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)

print(eye_colors)

# defaultdict(list,
#             {'blue': ['john', 'jill'],
#              'brown': ['jack'],
#              'unknown': ['eric', 'michael']})

# Let's look at another example where we use a non-deterministic factory. We could make a database call, an API call,
# and so on. To keep this simple I'm going to use the current time as my default.
#
# In this example we want to keep track of how many times certain functions are being called, as well as
# when they were first called. To do this I want to be able to decorate the functions I want to keep track of,
# and I want to be able to specify the dictionary that should be used so I can keep a reference
# to it so I can examine the results.

from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps


def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)

        return wrapper

    return Stats(decorator, d)

stats = function_stats()
dict(stats.data)
# {}

@stats.decorator
def func_1():
    pass

@stats.decorator
def func_2(x, y):
    pass
dict(stats.data)
# {}

func_1()
dict(stats.data)
# {'func_1': {'count': 1,
#   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)}}

func_1()
dict(stats.data)
# {'func_1': {'count': 2,
#   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)}}

func_2(10, 20)
dict(stats.data)
# {'func_1': {'count': 2,
#   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)},
#  'func_2': {'count': 1,
#   'first_called': datetime.datetime(2018, 12, 29, 22, 43, 49, 714090)}}

