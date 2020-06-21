# Custom JSON Serialization
# As we saw in the previous video, certain data types cannot be serialized to JSON using Python's defaults.
# Here's a simple example of this:

from datetime import datetime

current = datetime.utcnow()

print(current)
# datetime.datetime(2018, 12, 29, 22, 26, 35, 671836)

print('#' * 52 + '  As we can see, this is a `datetime` object.')

import json

# json.dumps(current)  #  TypeError: Object of type 'datetime' is not JSON serializable
# TypeError: Object of type 'datetime' is not JSON serializable
# As we can see Python raises a TypeError exception, stating that datetime objects are not JSON serializable.
# So, we'll need to come up with our own serialization format.
# For datetimes, the most common format is the ISO 8601 format - you can read up more about it here
# (https://en.wikipedia.org/wiki/ISO_8601), but basically the format is:
# YYYY-MM-DD T HH:MM:SS
# There are some variations for encoding timezones, but to keep things simple I am going to use timezone naive
# timestamps, and just use UTC everywhere.
# We could use Python's string representation for datetimes:

print()
print('#' * 52 + '  We could use Pythons string representation for datetimes:')
print(str(current))
# '2018-12-29 22:26:35.671836'
# ######################################################################################################################

print('#' * 52 + '  but this is not quite ISO-8601. We could write a custom formatter ourselves:')

def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

# (If you want more info and options on date and time formatting/parsing using strftime and strptime,
# which essentially pass through to their C counterparts, you can see the Python docs here:
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)

print(format_iso(current))
# '2018-12-29T22:26:35'
# ######################################################################################################################

print('#' * 52 + '  But Python actually provides us a function to do the same:')

print(current.isoformat())
# 2018-12-29T22:26:35.671836'
# ######################################################################################################################

# This is almost identical to our custom representation, but also includes fractional seconds.
# If you don't want fractional seconds in your representation, then you'll have to write some custom code like the one
# above. I'm just going to use Python's ISO-8601 representation. And now let's serialize our datetime object to JSON:
print('#' * 52 + '  This is'
                 '  almost identical to our custom representation, but also includes fractional seconds.')
print('#' * 52 + '  If you dont want fractional seconds in your representation, '
                 '  then you will have to write some custom code like the one above.')
print()

log_record = {'time': datetime.utcnow().isoformat(), 'message': 'testing'}
print(json.dumps(log_record))
# '{"time": "2018-12-29T22:26:42.083020", "message": "testing"}'
# ######################################################################################################################

print('#' * 52 + '  OK, this works, but this is far from ideal.')
print('#' * 52 + '  Normally, our dictionary will contain the `datetime` object, not its string representation.')

log_record = {'time': datetime.utcnow(), 'message': 'testing'}
# The problem is that log_record is now not JSON serializable!
# What we have to do is write custom code to replace non-JSON serializable objects in our dictionary with custom
# representations. This can quickly become tedious and unmanageable if we deal with many dictionaries,
# and arbitrary structures.
# Fortunately, Python's dump and dumps functions have some ways for us to define general serializations for
# non-standard JSON objects.
# The simplest way is to specify a function that dump/dumps will call when it encounters something it cannot serialize

def format_iso(dt):
    return dt.isoformat()

print(json.dumps(log_record, default=format_iso))
# '{"time": "2018-12-29T22:26:42.532485", "message": "testing"}'
# ######################################################################################################################

print('#' * 52 + '  This will work even if we have more than one date in our dictionary:')

log_record = {
    'time1': datetime.utcnow(),
    'time2': datetime.utcnow(),
    'message': 'Testing...'
}

print(json.dumps(log_record, default=format_iso))
# '{"time1": "2018-12-29T22:26:43.296170", "time2": "2018-12-29T22:26:43.296171", "message": "Testing..."}'
# ######################################################################################################################

print('#' * 52 + '  So this works, but what happens if we introduce another non-serializable object:')

log_record = {
    'time': datetime.utcnow(),
    'message': 'Testing...',
    'other': {'a', 'b', 'c'}
}

# json.dumps(log_record, default=format_iso) # AttributeError: 'set' object has no attribute 'isoformat'
# AttributeError: 'set' object has no attribute 'isoformat'
# As you can see, Python encountered that set, and therefore called the default callable - but that callable was not
# designed to handle sets, and so we end up with an exception in the format_iso callable instead
# We can remedy this by essentially adding code to our function to make it handle various data types.
# Essentially creating a dispatcher - this should remind you of the single-dispatch generic function decorator
# available in the functools module which we discussed in an earlier part of this series. You can also view more
# info about it here: https://docs.python.org/3/library/functools.html#functools.singledispatch
# Let's first write it without the decorator to make sure we have our code correct:

print('#' * 52 + '  Lets first write it without the decorator to make sure we have our code correct:')

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)

print(json.dumps(log_record, default=custom_json_formatter))
# '{"time": "2018-12-29T22:26:43.760863", "message": "Testing...", "other": ["c", "a", "b"]}'
# ######################################################################################################################

print('#' * 52 + '  To make things a little more interesting, lets throw in a custom object as well:')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt.isoformat()
        }


p = Person('John', 82)
print(p)
print(p.toJSON())
# Person(name=John, age=82)
# {'name': 'John', 'age': 82, 'create_dt': '2018-12-29T22:26:45.066252'}
# ######################################################################################################################

print('#' * 52 + '  And we modify our custom JSON formatter as follows:')


def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person):
        return arg.toJSON()


log_record = dict(time=datetime.utcnow(),
                  message='Created new person record',
                  person=p)

print(json.dumps(log_record, default=custom_json_formatter))
# '{"time": "2018-12-29T22:26:45.769929", "message": "Created new person record", "person": {"name": "John", "age": 82, "create_dt": "2018-12-29T22:26:45.066252"}}'
# ######################################################################################################################

print(json.dumps(log_record, default=custom_json_formatter, indent=2))
# {
#   "time": "2018-12-29T22:26:45.769929",
#   "message": "Created new person record",
#   "person": {
#     "name": "John",
#     "age": 82,
#     "create_dt": "2018-12-29T22:26:45.066252"
#   }
# }
# ######################################################################################################################

print('#' * 52 + '  One thing to note here is that for the `Person` class'
                 '  we returned a formatted string for the `created_dt` attribute.')
print('#' * 52 + '  We dont actually need to do this - we can simply return a `datetime` object and'
                 '  let `custom_json_formatter` handle serializing the `datetime` object:')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt
        }


p = Person('Monty', 100)

log_record = dict(time=datetime.utcnow(),
                  message='Created new person record',
                  person=p)

print(json.dumps(log_record, default=custom_json_formatter, indent=2))
# {
#   "time": "2018-12-29T22:26:47.029102",
#   "message": "Created new person record",
#   "person": {
#     "name": "Monty",
#     "age": 100,
#     "create_dt": "2018-12-29T22:26:46.749022"
#   }
# }
# ######################################################################################################################

print('#' * 52 + '  In fact, we could simplify our class further by simply returning a dict of the attributes, '
                 '  since in this case we want to serialize everything as is.')
print('#' * 52 + '  But using the `toJSON` callable means we can customize exactly '
                 '  how we want out objects to be serialized.')
print('#' * 52 + '  So, if we were +not particular about the serialization we could do this:')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return vars(self)

p = Person('Python', 27)

print(p.toJSON())
# {'name': 'Python',
#  'age': 27,
#  'create_dt': datetime.datetime(2018, 12, 29, 22, 26, 47, 973930)}
# ######################################################################################################################

print()
print()
print()
print('#' * 52 + '  ')

log_record['person'] = p
print(log_record)
# {'time': datetime.datetime(2018, 12, 29, 22, 26, 47, 29102), 'message': 'Created new person record', 'person': Person(name=Python, age=27)}
# ######################################################################################################################

print(json.dumps(log_record, default=custom_json_formatter, indent=2))
# {
#   "time": "2018-12-29T22:26:47.029102",
#   "message": "Created new person record",
#   "person": {
#     "name": "Python",
#     "age": 27,
#     "create_dt": "2018-12-29T22:26:47.973930"
#   }
# }
# ######################################################################################################################

print('#' * 52 + '  In fact, we could use this approach in our custom formatter - '
                 '  if an object does not have a `toJSON` callable,')
print('#' * 52 + '  we will just use a dictionary of the attributes - it it has any, '
                 '  it might not (like a complex number or a set as examples), '
                 '  so we need to watch out for that as well.')

print('toJSON' in vars(Person))
# True
# ######################################################################################################################

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)


print('#' * 52 + '  Lets create another custom class that does not have a `toJSON` method:')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


pt1 = Point(10, 10)

print(vars(pt1))
# {'x': 10, 'y': 10}
# ######################################################################################################################

log_record = dict(time=datetime.utcnow(),
                  message='Created new point',
                  point=pt1,
                  created_by=p)

print(log_record)
# {'time': datetime.datetime(2018, 12, 29, 22, 26, 50, 955039),
#  'message': 'Created new point',
#  'point': Point(x=10, y=10),
#  'created_by': Person(name=Python, age=27)}
# ######################################################################################################################

print('#' * 52 + '  And we can now serialize it to JSON:')

print(json.dumps(log_record, default=custom_json_formatter, indent=2))
# {
#   "time": "2018-12-29T22:26:50.955039",
#   "message": "Created new point",
#   "point": {
#     "x": 10,
#     "y": 10
#   },
#   "created_by": {
#     "name": "Python",
#     "age": 27,
#     "create_dt": "2018-12-29T22:26:47.973930"
#   }
# }
# ######################################################################################################################

print('#' * 52 + '  So now, lets re-write our custom json formatter using the generic single dispatch decorator'
                 '  I mentioned earlier:')

from functools import singledispatch

# Our default approach is going to first try to use toJSON, if not it will try to use vars, and it that still fails
# we'll use the string representation, whatever that happens to be:

@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON...')
        return arg.toJSON()
    except AttributeError:
        print('\tfailed - trying to use vars...')
        try:
            return vars(arg)
        except TypeError:
            print('\tfailed - using string representation...')
            return str(arg)

# And now we 'register' other data types:

@json_format.register(datetime)
def _(arg):
    return arg.isoformat()


@json_format.register(set)
def _(arg):
    return list(arg)

print(json.dumps(log_record, default=json_format, indent=2))
# Point(x=10, y=10)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# {
#   "time": "2018-12-29T22:26:50.955039",
#   "message": "Created new point",
#   "point": {
#     "x": 10,
#     "y": 10
#   },
#   "created_by": {
#     "name": "Python",
#     "age": 27,
#     "create_dt": "2018-12-29T22:26:47.973930"
#   }
# }
# ######################################################################################################################

print('#' * 52 + '  Lets change our Person class to emit some custom JSON instead of just using `vars`:')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

    def toJSON(self):
        return dict(name=self.name)

p = Person('Python', 27)
log_record['created_by'] = p
print(json.dumps(log_record, default=json_format, indent=2))
# Point(x=10, y=10)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# {
#   "time": "2018-12-29T22:26:50.955039",
#   "message": "Created new point",
#   "point": {
#     "x": 10,
#     "y": 10
#   },
#   "created_by": {
#     "name": "Python"
#   }
# }
# ######################################################################################################################

print('#' * 52 + '  The way we wrote our default formatter,'
                 '  means that we can now also represent other unexpected data types, '
                 '  but using each objects string representation.')
print('#' * 52 + '  If that is not acceptable, we can either not do this and let a `TypeError` exception get generated,'
                 '  or register more custom formatters:')

from decimal import Decimal
from fractions import Fraction

print(json.dumps(dict(a=1 + 1j,
                      b=Decimal('0.5'),
                      c=Fraction(1, 3),
                      p=Person('Python', 27),
                      pt=Point(0, 0),
                      time=datetime.utcnow()
                      ),
                 default=json_format))
# (1+1j)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# 0.5
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# 1/3
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# Point(x=0, y=0)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# '{"a": "(1+1j)", "b": "0.5", "c": "1/3", "p": {"name": "Python"}, "pt": {"x": 0, "y": 0}, "time": "2018-12-29T22:26:54.860340"}'
# ######################################################################################################################

print('#' * 52 + '  Now, suppose we dont want that default representation for `Decimals` -'
                 '  we want to serialize it in this form: `Decimal(0.5)`.')
print('#' * 52 + '  All we need to do is to register a new function to serialize `Decimal` types:')


@json_format.register(Decimal)
def _(arg):
    return f'Decimal({str(arg)})'


print(json.dumps(dict(a=1 + 1j,
                      b=Decimal(0.5),
                      c=Fraction(1, 3),
                      p=Person('Python', 27),
                      pt=Point(0, 0),
                      time=datetime.utcnow()
                      ),
                 default=json_format))
# (1+1j)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# 1/3
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# Point(x=0, y=0)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# '{"a": "(1+1j)", "b": "Decimal(0.5)", "c": "1/3", "p": {"name": "Python"}, "pt": {"x": 0, "y": 0}, "time": "2018-12-29T22:26:55.491606"}'
# ######################################################################################################################

print(
    '#' * 52 + '  One last example that clearly shows the `json_format` function gets called recursively when needed:')

print(json.dumps(dict(pt = Point(Person('Python', 27), 2+2j)),
          default=json_format, indent=2))
# Point(x=Person(name=Python, age=27), y=(2+2j))
# 	trying to use toJSON...
# 	failed - trying to use vars...
# Person(name=Python, age=27)
# 	trying to use toJSON...
# (2+2j)
# 	trying to use toJSON...
# 	failed - trying to use vars...
# 	failed - using string representation...
# {
#   "pt": {
#     "x": {
#       "name": "Python"
#     },
#     "y": "(2+2j)"
#   }
# }
# ######################################################################################################################
