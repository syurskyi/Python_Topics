from datetime import datetime

current = datetime.utcnow()

print(current)

print('#' * 52 + '  As we can see, this is a `datetime` object.')

import json

# json.dumps(current)  #  TypeError: Object of type 'datetime' is not JSON serializable

print()
print('#' * 52 + '  We could use Pythons string representation for datetimes:')
print(str(current))

print('#' * 52 + '  but this is not quite ISO-8601. We could write a custom formatter ourselves:')


def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')


print(format_iso(current))

print('#' * 52 + '  But Python actually provides us a function to do the same:')

print(current.isoformat())

print('#' * 52 + '  This is'
                 '  almost identical to our custom representation, but also includes fractional seconds.')
print('#' * 52 + '  If you dont want fractional seconds in your representation, '
                 '  then you will have to write some custom code like the one above.')
print()

log_record = {'time': datetime.utcnow().isoformat(), 'message': 'testing'}
print(json.dumps(log_record))

print('#' * 52 + '  OK, this works, but this is far from ideal.')
print('#' * 52 + '  Normally, our dictionary will contain the `datetime` object, not its string representation.')

log_record = {'time': datetime.utcnow(), 'message': 'testing'}


def format_iso(dt):
    return dt.isoformat()


print(json.dumps(log_record, default=format_iso))

print('#' * 52 + '  This will work even if we have more than one date in our dictionary:')

log_record = {
    'time1': datetime.utcnow(),
    'time2': datetime.utcnow(),
    'message': 'Testing...'
}

print(json.dumps(log_record, default=format_iso))

print('#' * 52 + '  So this works, but what happens if we introduce another non-serializable object:')

log_record = {
    'time': datetime.utcnow(),
    'message': 'Testing...',
    'other': {'a', 'b', 'c'}
}

# json.dumps(log_record, default=format_iso) # AttributeError: 'set' object has no attribute 'isoformat'

print('#' * 52 + '  Lets first write it without the decorator to make sure we have our code correct:')


def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)


print(json.dumps(log_record, default=custom_json_formatter))

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

print(json.dumps(log_record, default=custom_json_formatter, indent=2))

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

print()
print()
print()
print('#' * 52 + '  ')

log_record['person'] = p
print(log_record)

print(json.dumps(log_record, default=custom_json_formatter, indent=2))

print('#' * 52 + '  In fact, we could use this approach in our custom formatter - '
                 '  if an object does not have a `toJSON` callable,')
print('#' * 52 + '  we will just use a dictionary of the attributes - it it has any, '
                 '  it might not (like a complex number or a set as examples), '
                 '  so we need to watch out for that as well.')

print('toJSON' in vars(Person))


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

log_record = dict(time=datetime.utcnow(),
                  message='Created new point',
                  point=pt1,
                  created_by=p)

print(log_record)

print('#' * 52 + '  And we can now serialize it to JSON:')

print(json.dumps(log_record, default=custom_json_formatter, indent=2))

print('#' * 52 + '  So now, lets re-write our custom json formatter using the generic single dispatch decorator'
                 '  I mentioned earlier:')

from functools import singledispatch


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


@json_format.register(datetime)
def _(arg):
    return arg.isoformat()


@json_format.register(set)
def _(arg):
    return list(arg)


print(json.dumps(log_record, default=json_format, indent=2))

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

print(
    '#' * 52 + '  One last example that clearly shows the `json_format` function gets called recursively when needed:')

print(json.dumps(dict(pt = Point(Person('Python', 27), 2+2j)),
          default=json_format, indent=2))