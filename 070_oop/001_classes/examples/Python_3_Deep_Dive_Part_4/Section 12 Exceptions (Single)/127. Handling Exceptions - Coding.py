# -*- coding: utf-8 -*-
'''
### Handling Exceptions
'''

'''
We'll come back to how we can raise exceptions, but we've used it before, so I'll use it again now without explanation, 
just so we can raise some exceptions to examine exception **handling**.
'''

raise ValueError('custom exception')


# '''
# If this exception had occured at the module level when running the module, the Python application would exit.
# We did not **handle the exception, so the exception propagated all the way to the top and ended up aborting the
# program execution.


'''
In here though, Jupyter basically handles any exception (prints it out and silences it) so our notebook does not crash! 
(By the way, this is a very good use case for a bare exception handler!)
Let's try a simple handler first:
'''

try:
    raise ValueError('custom message')
except ValueError as ex:
    print(ex)

'''
As you can see, the string representation of the `ValueError` exception object is just the custom message we supplied 
as an argument to the exception. Most standard exceptions will actually support multiple arguments in their constructor, 
so we can actually do something like this:
'''

try:
    raise ValueError('custom message', 'secondary message')
except ValueError as ex:
    print(ex)

'''
Alternatively, we could use the `repr()` of the exception when printing it out:
'''

try:
    raise ValueError('custom message', 'secondary message')
except ValueError as ex:
    print(repr(ex))

'''
When we guard code (in a `try` block), we can handle different exception types in separate exception **handlers**:
'''

def func_1():
    raise ValueError('bad value')
    
try:
    func_1()
except ValueError as ex:
    print('handling a value error', repr(ex))
except IndexError as ex:
    print('handling an index error', repr(ex))

'''
But if `func_1` caused an `IndexError` exception to be raised, our second handler would catch it:
'''

def func_1():
    raise IndexError('bad index')
    
try:
    func_1()
except ValueError as ex:
    print('handling a value error', repr(ex))
except IndexError as ex:
    print('handling an index error', repr(ex))

'''
The first exception handler that "matches" (subclass!) the exception type will be used - so be careful about not 
catching broad exceptions first. For example, this will not handle the exception in the `ValueError` handler, 
because it is a subclass of `Exception` and that handler is defined first:
'''

try:
    raise ValueError('value error')
except Exception as ex:
    print('handling Exception', repr(ex))
except ValueError as ex:
    print('handling ValueError', repr(ex))


'''
Note that the exception is still an instance of `ValueError`, but is being handled by the code in the `except Exception` 
handler. If we write exception handlers, and none of them match the exception type, then the exception is essentially 
unhandled,  and it will propagate up:
'''

try:
    raise KeyError('bad key')
except ValueError:
    print('handling value error...')
except IndexError:
    print('handling index error...')

'''
The `finally` block is guaranteed to execute, whether an exception is raised or not, and whether it is handled or not!
'''

try:
    raise ValueError('bad value')
except ValueError:
    print('handling value error...')
finally:
    print('running finally...')

'''
If no exception occurs:
'''

try:
    pass
except ValueError:
    print('handling value error...')
finally:
    print('running finally...')    

'''
And with an unhandled exception:
'''

try:
    raise ValueError('bad value')
except IndexError:
    print('handling index error...')
finally:
    print('running finally...')

'''
This means that the `finally` block will execute even if there are no exception handlers defined, and whether or not 
an exception is raised:
'''

try:
    pass
finally:
    print('finally...')

try:
    raise ValueError()
finally:
    print('finally...')

'''
The except clause on the other hand is a block that excues if no exceptions occurred - it requires at least one 
except clause to be present:
'''

try:
    pass
except ValueError:
    print('value error...')
else:
    print('no exception occurred...')

try:
    raise ValueError();
except ValueError:
    print('value error...')
else:
    print('no exception occurred...')

try:
    raise ValueError()
except IndexError:
    print('index error...')
else:
    print('no exception occurred...')

'''
Some developers often ignore the `else` clause altogether, and write the following:
'''

try:
    pass
except ValueError:
    print('value error...')
else:
    print('no exception occurred...')

'''
this way:
'''

try:
    pass
except ValueError:
    print('value error...')
print('no exception occurred')

'''
These two are in fact **not** equivalent!
What happens if a `ValueError` exception does occur?
'''

try:
    raise ValueError()
except ValueError:
    print('value error...')
else:
    print('no exception occurred...')

try:
    raise ValueError()
except ValueError:
    print('value error...')
print('no exception occurred')

'''
As you can see we do **not** have the same functionality.
`try` statement can be nested. Obviously they can be nested if one `try` clause calls another function that itself 
contains a `try`. But they can also be nested, one within the other directly.
Let's first see the direct nesting:
Suppose we want to create a list of `Person` objects from a deserialized `json` object:
'''
import json

json_data = """{
    "Alex": {"age": 18},
    "Bryan": {"age": 21, "city": "London"},
    "Guido": {"age": "unknown"}
}"""

'''
First we can deserialize the json string into a dictionary:
'''

data = json.loads(json_data)
print(data)

'''
Next we are going to create a list of `Person` objects, and iterate through the properties of each person in the `data` 
dict and set them directly on the `Person` instance. 
Firstly, the `city` attribute is going to be a problem since `Person` only has two slots defined (`name` and `age`). 
This will be an `AttributeError`.
Secondly, `Guido`'s age is not a valid value - this is going to cause a `ValueError`.
'''

class Person:
    __slots__ = 'name', '_age'
    
    def __init__(self, name):
        self.name = name
        self._age = None
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError('Invalid age')
            
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

'''
The way we want to handle this is that if some "extra" attributes exist we just want to ignore them, but if a value is 
of the wrong type, we do not want to create the object in our list.
'''

persons = []
for name, attributes in data.items():
    try:
        p = Person(name)
        
        for attrib_name, attrib_value in attributes.items():
            try:
                setattr(p, attrib_name, attrib_value)
            except AttributeError:
                print(f'ignoring attribute: {name}.{attrib_name}={attrib_value}')
    except ValueError as ex:
        print(f'Data for Person({name}) contains an invalid attribute value: {ex}')
    else:
        # note that this runs if the outer try does not encounter an exception
        # since the inner try catches and does not propagate an `AttributeError`
        # this does not affect this else - the outer try never sees the inner exception
        # since it was handled (and essentially silenced)
        persons.append(p)
        
print(persons)

'''
While we could certainly handle the `ValueError` in the nested `for` loop, it makes the logic a bit more difficult:
'''

persons = []
for name, attributes in data.items():
    p = Person(name)

    for attrib_name, attrib_value in attributes.items():
        skip_person = False
        try:
            setattr(p, attrib_name, attrib_value)
        except AttributeError:
            print(f'ignoring attribute: {name}.{attrib_name}={attrib_value}')
        except ValueError as ex:
            print(f'Data for Person({name}) contains an invalid attribute value: {ex}')
            skip_person = True
            break
    if not skip_person:
        persons.append(p)
        
print(persons)

'''
Obviously the nested `try` is more elegant, and easier to understand.
Exception handlers may also be nested a different levels of the call stack, and either an exception is handled, or it 
is propagated up.
Here we want to create a simple function to transform `0`, `1`, `"0"`, `"1"`, `"T"`, `"F"`, `"True"`, `"False"`, 
`True` and `False` into the equivalent boolean type, as well as case insensitive versions of the strings.
'''

def convert_int(val):
    if not isinstance(val, int):  # remember this will work for booleans too!
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError("Integer values 0 or 1 only")
    return bool(val)


def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()
        
    val = val.casefold()  # for case-insensitive comparisons
    if val in {'0', 'f', 'false'}:
        return False
    elif val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False (case insensitive)')

'''
Now let's write the main converter function:
'''

class ConversionError(Exception):
    pass

def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            # it wasn't an int/bool, so let's try it as a string
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool')
    except ValueError as ex:
        # this will catch ValueError exceptions from either convert_int or convert_str
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b
    

'''
The way we have this written, a `ConversionError` exception will be raised, both on a type error, and a value error.
Notice how we are using exception handling to control the execution flow of our code.
In particular, we are not testing for conditions prior to attempting something (i.e. we do not check if something is 
an instance of an `int` before calling `convert_int` - we just try it, and catch the exception if that did not work, 
and then proceed to do the same with `convert_str`).
This is called "asking for forgiveness later". Just try the code, and handle the exception (ask forgiveness) later.
Now we can convert our values:
'''

values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)

    print(value, result)

'''
If having three lefvels of nested try's in a single fucntion is too much for you, we could simplify it a little, 
at the expense of some repetitive code (usually not a good idea):
'''

class ConversionError(Exception):
    pass

def make_bool(val):
    try:
        b = convert_int(val)
    except TypeError:
        pass  # for now we ignore type errors
    except ValueError as ex:
        # it wasn't an int/bool, so let's try it as a string
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b
    
    # reached here so we must have had a type error
    try:
        b = convert_str(val)
    except TypeError:
        pass  # silence this again
    except ValueError as ex:
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b
        
    # reached here, so neither an int nor a string
    raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool')


values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)

    print(value, result)


'''
We could have tried a different strategy here, the "look before you leap" strategy. In this case we try to not to 
cause exceptions by guarding against them.
Here's an equivalent functionality using this approach. Note that we cannot really break out the `int` and `str` 
conversions cleanly, because we need to test for admissible types and values before we even try the conversion:
'''

def make_bool(val):
    if isinstance(val, int):
        if val in {0, 1}:
            return bool(val)
        else:
            raise ConversionError('Invalid integer value.')
    if isinstance(val, str):
        if val.casefold() in {'1', 'true', 't'}:
            return True
        if val.casefold() in {'0', 'false', 'f'}:
            return False
        raise ConversionError('Invalid string value')
    raise ConversionError('Invalid type')

values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)

    print(value, result)

'''
Usually the "ask forgiveness later" approach is favored over the "look before you leap" approach in Python. 
This is sometimes referred to as **EAFP** - easier to ask for permission.
But the above example shows you that that is not always clear cut - honestly I think the second version is more 
comprehensible than the first.
Here's a much clear example. Let's write a function that needs to use an element at some index of a sequence type, 
and use a default value it it's not there:
The "forgiveness" approach first:
'''

def get_item_forgive_me(seq, idx, default=None):
    try:
        return seq[idx]
    except (IndexError, TypeError, KeyError):
        # catch either not indexable (TypeError), or index out of bounds, 
        # or even a KeyError for mapping types
        return default

'''
The "ask permission" first is not that simple! How do we determine if an object is a sequence type?
'''

def get_item_ask_perm(seq, idx, default=None):
    if hasattr(seq, '__getitem__'):
        if idx < len(seq):
            return seq[idx]
    return default

'''
The first one works quite well:
'''

get_item_forgive_me([1, 2, 3], 0)
get_item_forgive_me([1, 2, 3], 10, 'Nope')

'''
The second one seems to work ok:
'''

get_item_ask_perm([1, 2, 3], 0)
get_item_ask_perm([1, 2, 3], 10, 'Nope')

'''
But what about this:
'''
get_item_forgive_me({'a': 100}, 'a')
get_item_ask_perm({'a': 1}, 'a')

'''
So, now we would have to do a lot more work to support getting a key from a mapping using this approach. 
The dictionary has a `__getitem__` method, but does not support numerical indexing.
We could get bogged down in more and more checks:
'''

def get_item_ask_perm(seq, idx, default=None):
    if hasattr(seq, '__getitem__'):
        # could be sequence type or mapping type, or something else altogether??
        if isinstance(seq, dict):
            return seq.get(idx, default)
        elif isinstance(idx, int):
            # looks like a numerical index...
            if idx < len(seq):
                return seq[idx]
    return default


'''
That fixes the problem somewhat:
'''

get_item_ask_perm({'a': 100}, 'a')
get_item_ask_perm([1, 2, 3], 0)

'''
But now we are also relying on the sequence type having a length!
'''
class ConstantSequence:
    def __init__(self, val):
        self.val = val
        
    def __getitem__(self, idx):
        return self.val

'''
This is a sequence, an infinite sequence in fact:
'''
seq = ConstantSequence(10)
seq[0]

'''
And watch what happens with both our functions:
'''
get_item_forgive_me(seq, 10, 'Nope')
get_item_ask_perm(seq, 10, 'Nope')

'''
And so on, we could really dig ourselves into a hole here. When all we're interested in in making this call `seq[idx]`, 
and using a default if that does not work.
And that's why EAFP is favored - in Python, we are more interested in can an object perform this type of work, versus
'''
