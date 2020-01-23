
'''
### Raising Exceptions
'''

'''
An exception workflow can be initiated by using the `raise` statement.
To *raise* an exception we need to `raise` an **instance** of an exception type (one that is a subclass of 
`BaseException`).
You cannot raise an instance of a class that is not a subclass of `BaseException`.
'''

class Person:
    pass

try:
    raise Person()
except TypeError as ex:
    print(repr(ex))

'''
All the standard exceptions derive from `BaseException` and it allows for any number of positional arguments in 
the initializer (`*args`). The only place those arguments are actually used in `BaseException` is in the `args` 
attribute and the string representations:
'''

ex = BaseException('a', 'b', 'c')
ex.args
str(ex)
repr(ex)

'''
This means that other standard exceptions, that inherit from `BaseException` support this too:
'''
ex = ValueError('a', 'b', 'c')
print(ex.args)
print(str(ex))
print(repr(ex))

'''
Often we only use a single argument, some type of explanatory message, but it is handy to have the option of extra 
arguments available.
So raising an exception is very easy:
'''

try:
    raise ValueError('some message here')
except ValueError as ex:
    print(repr(ex))

'''
But there are some useful variations on the `raise` statement.
Sometimes we want to catch an exception, try to handle it, maybe because we realize we can't handle that specific 
exception, or because we want to perform some action before letting the exception continue to propagate - 
essentially inserting ourselves in the propagation workflow, but letting it continue once we're done.
Here's a more concrete example:
'''
def div(a, b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging zero division exception: ', type(ex).__name__, ex.args)
        raise

div(1, 0)

'''
As you can see, we interrupted the flow, logged what we needed, and resume the propagation flow.
Sometimes we may want to change the particular exception we are raising - this is particularly useful when using 
custom exceptions, as we'll cover later.
But here's what I mean:
'''

class CustomError(Exception):
    """a custom exception"""
    
def my_func(a, b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging...')
        raise CustomError(*ex.args)


my_func(1, 0)


'''
So, the exception we obtained was a `CustomError` exception - what we substituted for the `ZeroDivisionError` 
exception that occurred.
One very important note here, is the traceback.
Notice how we can see precisely the exception stack - first a `ZeroDivisionError`, that then resulted in a `CustomError` 
exception.
Whenever we raise an exception in this way, the stack trace of the current exception is maintained and added to our 
new exception being raised.
We could see this nested more levels:
'''

try:
    raise ValueError('level 1')
except ValueError:
    try:
        raise TypeError('level 2')
    except TypeError:
        raise KeyError('level 3')

'''
As you can see the entire stack trace is preserved.
Sometimes we may want to modify whether we want to keep the original stack trace - we may be writing a function where 
the specific exceptions that result in the final exception we want to raise are implementation details we don't want
our user to have to wade through.
In that case, we can squash the current traceback completely, by using raise Exc from None - the from here tells 
Python what traceback to use - in this case `None`.
Let's see where this might be handy. Remember that set of functions we wrote earlier to convert a value to it's 
boolean equivalent?
Here it is again:
'''

class ConversionError(Exception):
    pass

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
And when we call the function with a bad value:
'''

make_bool('ABC')

'''
Notice how the stack trace is quite complicated. Do we really want users of our function to see this? The internal 
implementation details of our function is not of interest to them, we just want to raise a "clean" `ConversionError` 
exception.
We can do so by using `from None` when we raise our custom exception:
'''

class ConversionError(Exception):
    pass

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
        
def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            # it wasn't an int/bool, so let's try it as a string
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool') from None
    except ValueError as ex:
        # this will catch ValueError exceptions from either convert_int or convert_str
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}') from None
    else:
        return b
    
make_bool('ABC')
make_bool(1.0)

'''
As you can see, the traceback is much cleaner.
We can also be very specific as to which traceback to use when we raise an exception. 
'''

try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('value error occurred')

'''
Notice how the traceback contains the entire exception stack. We could of course remove it entirely:
'''

try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('value error occurred') from None

'''
But we could also choose to only skip `level2` by using the traceback from `level1`:
'''

try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('value error occurred') from ex_1

'''
As you can see, we used the traceback from `ex_1` when we raised our final `ValueError`.
This can be useful if you trap some exception, try to handle it, and in the process cause another exception to 
be raised. 
When you handle that secondary exception, you may very well consider it an implementation detail and wish to shield 
the user from that particular exception - but the original one is important enough to include it in the traceback.
Let's look at an example that uses the `convert_int` function from earlier. We know that if we pass it a non-integer
value, it will give us a type exception:
'''

convert_int(1.0)

'''
Now suppose we are writing a function that makes use of it:
'''

def calc(b):
    try:
        b_bool = convert_int(b)
    except TypeError as ex_1:
        # bad type, but maybe it was a float and we could try to convert it to an int first
        try:
            b_int = int(b)
        except (ValueError, TypeError):
            raise CustomError('Bad type')
            
        b_bool = convert_int(b_int)

    return b_bool   

calc(1), calc(0)
calc(1.0)
calc('A')

'''
As you can see we get an ugly stack trace here, that includes the exception when we tried to cast our argument 
to an int. We can hide it by using the traceback from `ex_1` instead:
'''

def calc(b):
    try:
        b_bool = convert_int(b)
    except TypeError as ex_1:
        # bad type, but maybe it was a float and we could try to convert it to an int first
        try:
            b_int = int(b)
        except (ValueError, TypeError):
            raise CustomError('Bad type') from ex_1
            
        b_bool = convert_int(b_int)

    return b_bool   


calc('ab')
