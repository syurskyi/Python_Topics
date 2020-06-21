# %%
'''
### Project 5 - Solution
'''

# %%
'''
Suppose we are writing an application that uses exceptions and we want our exception messages (and type) 
to be very consistent, as well as provide some way to easily list out all the possible exceptions used in our app.
'''

# %%
'''
Although there are many other approaches to doing this (as with any problem), let's use enumerations specifically 
to implement this functionality.
'''

# %%
'''
What we want is a mechanism whereby we can raise an exception this way:
'''

# %%
'''
```
AppException.Timeout.throw()
```
which will raise a custom exception `ConnectionException('100 - Timeout connecting to resource')`
'''

# %%
'''
And something like this as well:
```
AppException.NotAnInteger.throw()
```
which will raise a `ValueError('200 - Value is not an integer')`
'''

# %%
'''
This means our exception will need to contain the exception key (such as `Timeout` or `NotAnInteger`) as well as 
the exception class we want to raise, and the default message itself. We also want to have consistent error codes 
(integer values) for each exception.
We'll need to implement a `throw` method (we can't use the reserved name `raise`) that will raise the exception 
with the default message. In addition we'd like to be able to override the default message with a custom one if we 
prefer:
```
AppException.Timeout.throw('Timeout connecting to database')
```

We'll also need to implement some properties for the exception code, class (type), and message.
'''

# %%
'''
First let's create a few custom exceptions that we can use, but of course we can also use all 
the builtin exceptions too.
'''

# %%
class GenericException(Exception):
    pass

class Timeout(Exception):
    pass

# %%
'''
We'll come back to exceptions later and see why we may actually want to build a hierarchy of exception instead 
of this flat appropach I took here.
'''

# %%
from enum import Enum

# %%
'''
First we're going to need to store a tuple for each key's value and that tuple will need to contain the error code, 
the exception class, and a custom message. So three entities.
We'll use the same approach we took when we looked at extending enums, and use the `__new__` method to achieve our 
goals.    
'''

# %%
class AppException(Enum):
    Generic = (100, GenericException, 'Application exception.')
    Timeout = (101, Timeout, 'Timeout connecting to resource.')
    NotAnInteger = (200, ValueError, 'Value must be an integer.')
    NotAList = (201, ValueError, 'Value must be a list.')
    
    def __new__(cls, ex_code, ex_class, ex_message):
        # create a new instance of cls
        member = object.__new__(cls)
        
        # set up instance attributes
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member

# %%
'''
So this is a good start. We can use our enum this way:
'''

# %%
AppException.Timeout.value, AppException.Timeout.message, AppException.Timeout.exception

# %%
'''
So we could technically raise an exception directly from this:
'''

# %%
try:
    raise AppException.Timeout.exception(f'{AppException.Timeout.value} - {AppException.Timeout.message}')
except Timeout as ex:
    print(ex)

# %%
'''
But we really do not want to have to raise exceptions this way - it's a lot of typing. I also don't like using `value` 
for the exception code, I'd rather have a property called `code` that is maybe a better name for it.
'''

# %%
'''
So, we'll immplement a `code` property (we'll leave value as is, because we can look up an exception by it's code 
that way), and we'll implement a `raise` method to actually raise the exception for us.
'''

# %%
class AppException(Enum):
    Generic = (100, GenericException, 'Application exception.')
    TimeOut = (101, Timeout, 'Timeout connecting to resource.')
    NotAnInteger = (200, ValueError, 'Value must be an integer.')
    NotAList = (201, ValueError, 'Value must be a list.')
    
    def __new__(cls, ex_code, ex_class, ex_message):
        # create a new instance of cls
        member = object.__new__(cls)
        
        # set up instance attributes
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member
    
    @property
    def code(self):
        return self.value
    
    def throw(self):
        raise self.exception(f'{self.code} - {self.message}')

# %%
'''
Now it becomes much easier to raise an exception:
'''

# %%
try:
    AppException.NotAnInteger.throw()
except ValueError as ex:
    print(ex)

# %%
'''
We can easily access exceptions by name (key) or code (value):
'''

# %%
AppException.NotAList.code, AppException.NotAList.message

# %%
'''
or:
'''

# %%
AppException(201), AppException['NotAList']

# %%
'''
One additional thing is that I would like the ability to override the default error message. So let's add this 
to the `throw` method:
'''

# %%
class AppException(Enum):
    Generic = (100, GenericException, 'Application exception.')
    Timeout = (101, Timeout, 'Timeout connecting to resource.')
    NotAnInteger = (200, ValueError, 'Value must be an integer.')
    NotAList = (201, ValueError, 'Value must be a list.')
    
    def __new__(cls, ex_code, ex_class, ex_message):
        # create a new instance of cls
        member = object.__new__(cls)
        
        # set up instance attributes
        member._value_ = ex_code
        member.exception = ex_class
        member.message = ex_message
        return member
    
    @property
    def code(self):
        return self.value
    
    def throw(self, message=None):
        message = message or self.message
        raise self.exception(f'{self.code} - {message}')

# %%
try:
    AppException.Timeout.throw()
except Exception as ex:
    print(ex)

# %%
try:
    AppException.Timeout.throw('Timeout connecting to database.')
except Exception as ex:
    print(ex)

# %%
'''
And of course we can list out all the errors in our app:
'''

# %%
list(AppException)

# %%
'''
We can get a more usable list of exception names, codes and messages this way:
'''

# %%
[(ex.name, ex.code, ex.message) for ex in AppException]