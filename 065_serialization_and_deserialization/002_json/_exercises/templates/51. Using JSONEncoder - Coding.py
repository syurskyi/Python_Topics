import json

default_encoder = json.JSONEncoder()
print(default_encoder.encode([1, 2, 3]))

print('#' * 52 + '  And for non-supported objects:')

# default_encoder.encode(1+1j) #  TypeError: Object of type 'complex' is not JSON serializable

print('#' * 52 + '  We can actually extend this `JSONEncoder` class and override the `default` method')
print('#' * 52 + '  We can then add in support for whatever type we want to use, '
                 '  and pass any other types to the parent class to handle '
                 '  (either serialize the data or raise a `TypeError` exception). ')

import json
from datetime import datetime


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg)


custom_encoder = CustomJSONEncoder()
print(custom_encoder.encode(True))
print(custom_encoder.encode(datetime.utcnow()))

print('#' * 52 + '  And we can now use this custom encoder by specifying it when we use `dump`/`dumps`:')

print(json.dumps(dict(name='test', time=datetime.utcnow()), cls=CustomJSONEncoder))

print('#' * 52 + '  One thing to note is that for both the `default` approach, '
                 '  and the `cls` approach, our method / encoder will only be used for types that Python'
                 '  cannot already serialize on its own (strings, integers, lists, etc).')


def custom_encoder(arg):
    print('Custom encoder called...')
    if isinstance(arg, str):
        return f'some string: {arg}'


print(json.dumps({'name': 'Python'}, default=custom_encoder))

print('#' * 52 + '  ')
print('#' * 52 + '  ')
print('#' * 52 + '  ')

# help(json.dumps)

print('#' * 52 + '  ')
print('#' * 52 + '  And lets see the signature for `JSONEncoder`:')
print('#' * 52 + '  ')

# help(json.JSONEncoder)

d = {
    'a': float('inf'),
    'b': [1, 2, 3]
}

print(d)
print(type(d['a']))

print('#' * 52 + '  As you can see, that float is a special type of float - it represents + infinity.')

print(json.dumps(d))

print('#' * 52 + '  Yes, it does - but notice the output, `Infinity`. ')
print('#' * 52 + '  Technically this is not JSON...')
print('#' * 52 + '  So, if we want to be strict about this, and ensure we are not trying to serialize'
                 '  a value such as infinity, we would do this instead:')

# json.dumps(d, allow_nan=False) #  ValueError: Out of range float values are not JSON compliant

print('#' * 52 + '  What about trying to encode an invalid key (from JSONs perspective)::')

d = {10: "int", 10.5: "float", 1+1j: "complex"}

print(d)

print('#' * 52 + '  These are all valid Python dictionary keys, but what happens with JSON encoding?')

# json.dumps(d) # TypeError: keys must be a string

print('#' * 52 + '  As you can see we get an exception.')

print('#' * 52 + '  We may want to simply ignore that exception and not include the offending'
                 '  key/value pair in our serialization:')

print(json.dumps(d, skipkeys=True))

print('#' * 52 + '  And now we no longer get an exception, and the complex key was simply skipped.')
print('#' * 52 + '  We can even change how the serialization is rendered '
                 '  (which of course means we may no longer have actual JSON):')

d = {
    'name': 'Python',
    'age': 27,
    'created_by': 'Guido van Rossum',
    'list': [1, 2, 3]
}

print(json.dumps(d))

print(print(json.dumps(d, indent='---', separators=('', ' = '))))

print('#' * 52 + '  We can use this by the way, to create more compact JSON strings (uses less bytes):')

print(json.dumps(d))

print('#' * 52 + '  vs')

print(json.dumps(d, separators=(',', ':')))

print('#' * 52 + '  So, if we want to consistently use the same values for all those tweaks, '
                 '  we have to consistently remember to set the arguments correctly in the `dump`/`dumps` functions.')
print('#' * 52 + '  Instead, we could create a custom JSONEncoder class that pre-sets all these things, '
                 '  and just use that encoder - simpler than remembering all those arguments and their correct values:')


class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(skipkeys=True,
                         allow_nan=False,
                         indent='---',
                         separators=('', ' = ')
                         )

    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)

d = {
    'time': datetime.utcnow(),
    1+1j: "complex",
    'name': 'Python'
}

print(json.dumps(d, cls=CustomEncoder))

print('#' * 52 + '  Another thing I want to point out is that with both these methods'
                 '  we are not limited in what we emit as our JSON serialization.')
print('#' * 52 + '  For example, for a `datetime` object, we may want to emit not only the ISO formatted date,'
                 '  but maybe some additional fields, all nested within a JSON object:')


class CustomEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            obj = dict(
                datatype="datetime",
                iso=arg.isoformat(),
                date=arg.date().isoformat(),
                time=arg.time().isoformat(),
                year=arg.year,
                month=arg.month,
                day=arg.day,
                hour=arg.hour,
                minutes=arg.minute,
                seconds=arg.second
            )
            return obj
        else:
            return super().default(arg)
d = {
    'time': datetime.utcnow(),
    'message': 'Testing...'
}

print(json.dumps(d, cls=CustomEncoder, indent=2))




