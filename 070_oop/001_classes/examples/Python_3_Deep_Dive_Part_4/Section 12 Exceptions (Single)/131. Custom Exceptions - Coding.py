# %%
'''
### Custom Exceptions
'''

# %%
'''
We can create our own exception types, by simply inheriting from `Exception`. (Usually, we want to inherit from 
`Exception`, not `BaseException` since `BaseException` includes exceptions such as `SystemExit`, `KeyboardInterrupt` 
and a few others - our custom exceptions mostly do not fall under the same *base* type of exceptions, but rather under 
`Exception`. 
'''

# %%
'''
Plus, it is usually expected that custom exceptions inherit from `Exception`, and people will think that trapping 
`Exception` will trap your exceptions as well.
'''

# %%
'''
So, to create a custom exception we simply inherit from `Exception`, or any subclass thereof.
'''

# %%
class TimeoutError(Exception):
    """Timeout exception"""

# %%
'''
Note: we should really always provide a docstring for any class or function we create. If we do so, a docstring **is** 
a valid Python statement, and it is enough for an "empty" class - we do not need to use `pass`.
'''

# %%
'''
Now we can trap an instance of `TimeoutError` with `TimeoutError`, `Exception`, or even `BaseException`.
'''

# %%
try:
    raise TimeoutError('timeout occurred')
except TimeoutError as ex:
    print(ex)

# %%
'''
Note that we do now need to provide an `__init__` since that is inherited from `BaseException`, and we get the variable 
number of arguments functionality, as well as `args` and the traceback. It works just like any standard Python 
exception.
'''

# %%
'''
We don't have to inherit from `Exception`, we can inherit from any exception type, including our own custom exceptions.
'''

# %%
class ReadOnlyError(AttributeError):
    """Indicates an attribute is read-only"""

# %%
try:
    raise ReadOnlyError('Account number is read-only', 'BA10001')
except ReadOnlyError as ex:
    print(repr(ex))

# %%
'''
Often when we have a relatively complex application, we create our own hierarchy of exceptions, where we use some base 
exception for our application, and every other exception is a subclass of that exception.
'''

# %%
'''
For example, suppose we are writing a library that is used to scrape some web sites and extract product information 
and pricing.
'''

# %%
'''
Let's say our library's name is *WebScraper*.
'''

# %%
'''
We might first create a base exception for our library:
'''

# %%
class WebScraperException(Exception):
    """Base exception for WebScraper"""

# %%
class HTTPException(WebScraperException):
    """General HTTP exception for WebScraper"""
    
class InvalidUrlException(HTTPException):
    """Indicates the url is invalid (dns lookup fails)"""
    
class TimeoutException(HTTPException):
    """Indicates a general timeout exception in http connectivity"""
    
class PingTimeoutException(TimeoutException):
    """Ping time out"""
    
class LoadTimeoutException(TimeoutException):
    """Page load time out"""
    
class ParserException(WebScraperException):
    """General page parsing exception"""

# %%
'''
As you can see we have this hierarchy:
'''

# %%
'''
```
WebScraperException
   - HTTPException
       - InvalidUrlException
       - TimeoutException
           - PingTimeoutException
           - LoadTimeoutException
    - ParserException
```
'''

# %%
'''
Now someone using our library can expect to trap **any** exception we raise by catching the `WebScraperException` type, 
or anything more specific if they prefer:
'''

# %%
try:
    raise PingTimeoutException('Ping to www.... timed out')
except HTTPException as ex:
    print(repr(ex))

# %%
'''
or more broadly:
'''

# %%
try:
    raise PingTimeoutException('Ping time out')
except WebScraperException as ex:
    print(repr(ex))

# %%
'''
So this is very useful when we write modules or packages and want to keep our exception hierarchy neatly contained 
with some base exception class. This way, users of our class are not forced to use `except Exception` to trap exceptions 
we might raise from inside our library.
'''

# %%
'''
Custom exception classes are like any custom class, which means we can add custom attributes, properties and methods to 
the class.
'''

# %%
'''
This might be useful to provide additional context and functionality to our exceptions.
'''

# %%
'''
For example, suppose we are writing a REST API. When we raise a custom exception, we'll also want to return an HTTP 
exception response to the API caller. We could write code like this in our API calls:
'''

# %%
'''
Suppose we need to retrieve an account (by ID) from a database. Here I'm just going to mock this:
'''

# %%
class APIException(Exception):
    """Base API exception"""

# %%
class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""
    
class DBException(ApplicationException):
    """General database exception"""
    
class DBConnectionError(DBException):
    """Indicates an error connecting to database"""
    
class ClientException(APIException):
    """Indicates exception that was caused by user, not an internal error"""
    
class NotFoundError(ClientException):
    """Indicates resource was not found"""

class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""
    
    
class Account:
    def __init__(self, account_id, account_type):
        self.account_id = account_id
        self.account_type = account_type

# %%
'''
So we have this exception hierarchy:

```
APIException
   - ApplicationException (5xx errors)
       - DBException
           - DBConnectionError
   - ClientException
       - NotFoundError
       - NotAuthorizedError
```
'''

# %%
def lookup_account_by_id(account_id):
    # mock of various exceptions that could be raised getting an account from database
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid.')
        
    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database.')
    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read this account')
    elif account_id < 300:
        raise NotFoundError(f'Account not found.')
    else:
        return Account(account_id, 'Savings')

# %%
'''
Now suppose we have this endpoint for a **GET** on the **Account** resource, and we need to return the appropriate HTTP
exception, and message to the user.
'''

# %%
'''
We're going to make use of the `HTTPStatus` enumeration we have seen before.
'''

# %%
from http import HTTPStatus

# %%
def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except ApplicationException as ex:
        return HTTPStatus.INTERNAL_SERVER_ERROR, str(ex)
    except NotFoundError as ex:
        return HTTPStatus.NOT_FOUND, 'The account {} does not exist.'.format(account_id)
    except NotAuthorizedError as ex:
        return HTTPStatus.UNAUTHORIZED, 'You do not have the proper authorization.'
    except ClientException as ex:
        return HTTPStatus.BAD_REQUEST, str(ex)
    else:
        return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}

# %%
'''
Now when we call our end point with different account numbers:
'''

# %%
get_account('abc')

# %%
get_account(50)

# %%
get_account(150)

# %%
get_account(250)

# %%
get_account(350)

# %%
'''
As you can see this was quite a lot of exception handling we had to do. And really, the HTTP status and message shoudl 
remain consistent with any exception type.
'''

# %%
'''
So instead of dealing with it the way we did, we are going to do the work in the exception classes themselves.
'''

# %%
'''
First we know we need an `HTTPStatus` for each exception, as well as an error message to present to our user that may 
need to be different from the internal error message we would want to log for example.
'''

# %%
class APIException(Exception):
    """Base API exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."

# %%
'''
Now having the default `internal_err_msg` and `user_err_msg` is great, but what if we ever wanted to override it for 
some reason?
'''

# %%
'''
Let's create an `__init__` to take care of that:
'''

# %%
class APIException(Exception):
    """Base API exception"""
    
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
    def __init__(self, *args, user_err_msg = None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)
            
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

# %%
'''
And we can use this exception quite easily:
'''

# %%
try:
    raise APIException()
except APIException as ex:
    print(repr(ex))
    print(ex.user_err_msg)

# %%
'''
Or with a custom (internal) message:
'''

# %%
try:
    raise APIException('custom message...', 10, 20)
except APIException as ex:
    print(repr(ex))

# %%
'''
And of course, the user message can be customized too:
'''

# %%
try:
    raise APIException('custom message...', 10, 20, user_err_msg='custom user message')
except APIException as ex:
    print(repr(ex))
    print(ex.user_err_msg)

# %%
'''
While we're at it, we know that we'll need to return the same JSON format when an exception occurs - so let's write it 
into our base exception class:
'''

# %%
import json

class APIException(Exception):
    """Base API exception"""
    
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
    def __init__(self, *args, user_err_msg = None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)
            
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg
            
    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)

# %%
'''
Now we can easily use this base class, and get consistent results:
'''

# %%
try:
    raise APIException()
except APIException as ex:
    print(repr(ex), ex.to_json())

# %%
'''
And because we'll want to log exceptions, let's also write a logger directly into our base class:
'''

# %%
from datetime import datetime

class APIException(Exception):
    """Base API exception"""
    
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'API exception occurred.'
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
    def __init__(self, *args, user_err_msg = None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)
            
        if user_err_msg is not None:
            self.user_err_msg = user_err_msg
    
    def to_json(self):
        err_object = {'status': self.http_status, 'message': self.user_err_msg}
        return json.dumps(err_object)
    
    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.internal_err_msg,
            "args": self.args[1:]
        }
        print(f'EXCEPTION: {datetime.utcnow().isoformat()}: {exception}')

# %%
try:
    raise APIException()
except APIException as ex:
    ex.log_exception()
    print(ex.to_json())

# %%
'''
Now let's finish up our hierarchy:
'''

# %%
class ApplicationException(APIException):
    """Indicates an application error (not user caused) - 5xx HTTP type errors"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "Generic server side exception."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
class DBException(ApplicationException):
    """General database exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "Database exception."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
class DBConnectionError(DBException):
    """Indicates an error connecting to database"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "DB connection error."
    user_err_msg = "We are sorry. An unexpected error occurred on our end."
    
class ClientException(APIException):
    """Indicates exception that was caused by user, not an internal error"""
    http_status = HTTPStatus.BAD_REQUEST
    internal_err_msg = "Client submitted bad request."
    user_err_msg = "A bad request was received."
    
class NotFoundError(ClientException):
    """Indicates resource was not found"""
    http_status = HTTPStatus.NOT_FOUND
    internal_err_msg = "Resource was not found."
    user_err_msg = "Requested resource was not found."

class NotAuthorizedError(ClientException):
    """User is not authorized to perform requested action on resource"""
    http_status = HTTPStatus.UNAUTHORIZED
    internal_err_msg = "Client not authorized to perform operation."
    user_err_msg = "You are not authorized to perform this request."

# %%
'''
Also, since we have a but more functionality available to us with our exceptions, let's refine the function that raises 
these exceptions:
'''

# %%
def lookup_account_by_id(account_id):
    # mock of various exceptions that could be raised getting an account from database
    if not isinstance(account_id, int) or account_id <= 0:
        raise ClientException(f'Account number {account_id} is invalid.', 
                              f'account_id = {account_id}',
                              'type error - account number not an integer')
        
    if account_id < 100:
        raise DBConnectionError('Permanent failure connecting to database.', 'db=db01')
    elif account_id < 200:
        raise NotAuthorizedError('User does not have permissions to read this account', f'account_id={account_id}')
    elif account_id < 300:
        raise NotFoundError(f'Account not found.', f'account_id={account_id}')
    else:
        return Account(account_id, 'Savings')

# %%
'''
Now we can re-write our API endpoint and very easily handle those exceptions:
'''

# %%
def get_account(account_id):
    try:
        account = lookup_account_by_id(account_id)
    except APIException as ex:
        ex.log_exception()
        return ex.to_json()
    else:
        return HTTPStatus.OK, {"id": account.account_id, "type": account.account_type}

# %%
get_account('ABC')

# %%
get_account(50)

# %%
get_account(150)

# %%
get_account(250)

# %%
get_account(350)

# %%
'''
#### Inheriting from Multiple Exceptions
'''

# %%
'''
We haven't covered multiple inheritance yet, but Python supports it, and it is very easy to use to solve a specific 
problem we may encounter with exceptions, so i want to mention it here.
'''

# %%
'''
Although we may want to raise a custom exception for some specific error, sometimes we may be wondering whether 
to raise a built-in exception that would work just as well, or raise a custom exception.
'''

# %%
'''
Here's an example of where this might occur:
'''

# %%
'''
Suppose we have a custom exception we use to tell a user of our function/library that the value they provided to some 
function is not the right value - maybe it needs to be a integer greater than or equal to 0.
'''

# %%
'''
We might have a custom exception just for that - remember what we discussed earlier, we might want our application to 
raise custom exceptions for everything, based off some application base exception our users could broadly trap.
'''

# %%
class AppException(Exception):
    """generic application exception"""
    
class NegativeIntegerError(AppException):
    """Used to indicate an error when an integer is negative."""

# %%
def set_age(age):
    if age < 0:
        raise NegativeIntegerError('age cannot be negative')

# %%
try:
    set_age(-10)
except NegativeIntegerError as ex:
    print(repr(ex))

# %%
'''
But the problem is that this is also a `ValueError`, and our users may want to trap it as a `ValueError` for some 
reason, not a `NegativeIntegerError` (or `AppException` as is possible here).
'''

# %%
'''
The beauty of multiple inheritance is that we can have our custom exception inherit from **more than one** exception.
'''

# %%
'''
All we need to understand here, is that if we inherit from more than one class, then our subclass is considered 
a subclass of **both** parents.
'''

# %%
class BaseClass1:
    pass

class BaseClass2:
    pass

class MyClass(BaseClass1, BaseClass2):
    pass

# %%
issubclass(MyClass, BaseClass1)

# %%
issubclass(MyClass, BaseClass2)

# %%
'''
So, we can do the same thing with our exception:
'''

# %%
class NegativeIntegerError(AppException, ValueError):
    """Used to indicate an error when an integer is negative."""

# %%
'''
Now this exception is a subclass of **both** `AppException` and `ValueError`:
'''

# %%
issubclass(NegativeIntegerError, AppException)

# %%
issubclass(NegativeIntegerError, ValueError)

# %%
'''
And we can trap it with either of those exception types:
'''

# %%
def set_age(age):
    if age < 0:
        raise NegativeIntegerError('age cannot be negative')

# %%
try:
    set_age(-10)
except NegativeIntegerError as ex:
    print(repr(ex))

# %%
try:
    set_age(-10)
except ValueError as ex:
    print(repr(ex))

# %%
'''
So this solves the problem - deciding between a custom exception vs a standard exception - we can just use both 
(or more!)
'''