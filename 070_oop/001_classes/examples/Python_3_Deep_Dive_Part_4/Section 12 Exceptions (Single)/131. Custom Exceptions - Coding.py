#
# '''
# ### Custom Exceptions
# '''
#
# '''
# We can create our own exception types, by simply inheriting from `Exception`. (Usually, we want to inherit from
# `Exception`, not `BaseException` since `BaseException` includes exceptions such as `SystemExit`, `KeyboardInterrupt`
# and a few others - our custom exceptions mostly do not fall under the same *base* type of exceptions, but rather under
# `Exception`.
# Plus, it is usually expected that custom exceptions inherit from `Exception`, and people will think that trapping
# `Exception` will trap your exceptions as well.
# So, to create a custom exception we simply inherit from `Exception`, or any subclass thereof.
# '''
#
# c_ TimeoutError E..
#     """Timeout exception"""
#
# '''
# Note: we should really always provide a docstring for any class or function we create. If we do so, a docstring **is**
# a valid Python statement, and it is enough for an "empty" class - we do not need to use `pass`.
# Now we can trap an instance of `TimeoutError` with `TimeoutError`, `Exception`, or even `BaseException`.
# '''
#
# ___
#     r___ ? timeout occurred
# _____ ? __ ex
#     print ?
#
# '''
# Note that we do now need to provide an `__init__` since that is inherited from `BaseException`, and we get the variable
# number of arguments functionality, as well as `args` and the traceback. It works just like any standard Python
# exception.
# We don't have to inherit from `Exception`, we can inherit from any exception type, including our own custom exceptions.
# '''
#
# c_ ReadOnlyError A..
#     """Indicates an attribute is read-only"""
#
# ___
#     r___ ? Account number is read-only', 'BA10001')
# _____ ? __ ex
#     print(re.. ?
#
# '''
# Often when we have a relatively complex application, we create our own hierarchy of exceptions, where we use some base
# exception for our application, and every other exception is a subclass of that exception.
# For example, suppose we are writing a library that is used to scrape some web sites and extract product information
# and pricing.
# Let's say our library's name is *WebScraper*.
# We might first create a base exception for our library:
# '''
#
# c_ WebScraperException E..
#     """Base exception for WebScraper"""
#
#
# c_ HTTPException W..
#     """General HTTP exception for WebScraper"""
#
# c_ InvalidUrlException H..
#     """Indicates the url is invalid (dns lookup fails)"""
#
# c_ TimeoutException H..
#     """Indicates a general timeout exception in http connectivity"""
#
# c_ PingTimeoutException T..
#     """Ping time out"""
#
# c_ LoadTimeoutException T..
#     """Page load time out"""
#
# c_ ParserException W..
#     """General page parsing exception"""
#
# '''
# As you can see we have this hierarchy:
# '''
#
#
# '''
# ```
# WebScraperException
#    - HTTPException
#        - InvalidUrlException
#        - TimeoutException
#            - PingTimeoutException
#            - LoadTimeoutException
#     - ParserException
# ```
# '''
#
#
# '''
# Now someone using our library can expect to trap **any** exception we raise by catching the `WebScraperException` type,
# or anything more specific if they prefer:
# '''
#
# ___
#     r___ P.. Ping to www.... timed out
# _____ H.. __ ex
#     print(re.. ?
#
# '''
# or more broadly:
# '''
#
#
# ___
#     r___ P.. Ping time out
# _____ W.. __ ex
#     print re.. ?
#
#
# '''
# So this is very useful when we write modules or packages and want to keep our exception hierarchy neatly contained
# with some base exception class. This way, users of our class are not forced to use `except Exception` to trap exceptions
# we might raise from inside our library.
# Custom exception classes are like any custom class, which means we can add custom attributes, properties and methods to
# the class.
# This might be useful to provide additional context and functionality to our exceptions.
# For example, suppose we are writing a REST API. When we raise a custom exception, we'll also want to r_ an HTTP
# exception response to the API caller. We could write code like this in our API calls:
# Suppose we need to retrieve an account (by ID) from a database. Here I'm just going to mock this:
# '''
#
#
# c_ APIException E..
#     """Base API exception"""
#
#
# c_ ApplicationException A..
#     """Indicates an application error (not user caused) - 5xx HTTP type errors"""
#
# c_ DBException A..
#     """General database exception"""
#
# c_ DBConnectionError D..
#     """Indicates an error connecting to database"""
#
# c_ ClientException AP..
#     """Indicates exception that was caused by user, not an internal error"""
#
# c_ NotFoundError C..
#     """Indicates resource was not found"""
#
# c_ NotAuthorizedError C..
#     """User is not authorized to perform requested action on resource"""
#
#
# c_ Account
#     ___ -  ____ account_id account_type
#         ____.?  ?
#         ____.?  ?
#
#
# '''
# So we have this exception hierarchy:
#
# ```
# APIException
#    - ApplicationException (5xx errors)
#        - DBException
#            - DBConnectionError
#    - ClientException
#        - NotFoundError
#        - NotAuthorizedError
# ```
# '''
#
# ___ lookup_account_by_id(account_id):
#     # mock of various exceptions that could be raised getting an account from database
#     __ no. isi.. ? in. or ? <_ 0
#         r___ C.. _*Account number |?| is invalid.
#
#     __ ? < 100
#         r___ D.. Permanent failure connecting to database.
#     ____ ? < 200
#         r___ N.. User does not have permissions to read this account
#     ____ ? < 300
#         r___ N.. _*Account not found.
#     ____
#         r_ Account(account_id, 'Savings')
#
#
# '''
# Now suppose we have this endpoint for a **GET** on the **Account** resource, and we need to r_ the appropriate HTTP
# exception, and message to the user.
# We're going to make use of the `HTTPStatus` enumeration we have seen before.
# '''
#
#
# ____ http _______ HTTPStatus
#
#
# ___ get_account account_id
#     ___
#         account = l.. ?
#     _____ A.. __ ex
#         r_ HT__.I_S_E st. ?
#     _____ N.. __ ex
#         r_ HT__.N_F 'The account @ does not exist.'.f.. ?
#     _____ N.. __ ex
#         r_ HT__.UN.. You do not have the proper authorization.
#     _____ C.. __ ex
#         r_ HT__.B_R st. ?
#     ___
#         r_ HT__.O. "id": ac__.? "type": a__.a_t
#
# '''
# Now when we call our end point with different account numbers:
# '''
# get_account('abc')
# get_account(50)
# get_account(150)
# get_account(250)
# get_account(350)
#
# '''
# As you can see this was quite a lot of exception handling we had to do. And really, the HTTP status and message shoudl
# remain consistent with any exception type.
# So instead of dealing with it the way we did, we are going to do the work in the exception classes themselves.
# First we know we need an `HTTPStatus` for each exception, as well as an error message to present to our user that may
# need to be different from the internal error message we would want to log for example.
# '''
#
#
# c_ APIException E..
#     """Base API exception"""
#     http_status = HT__.I_S_E
#     internal_err_msg = 'API exception occurred.'
#     user_err_msg = "We are sorry. An unexpected error occurred on our end."
#
# '''
# Now having the default `internal_err_msg` and `user_err_msg` is great, but what if we ever wanted to override it for
# some reason?
# Let's create an `__init__` to take care of that:
# '''
#
#
# c_ APIException E..
#     """Base API exception"""
#
#     http_status = HT...I_S_E
#     internal_err_msg = 'API exception occurred.'
#     user_err_msg = "We are sorry. An unexpected error occurred on our end."
#
#     ___ - ____ $ user_err_msg _ N..
#         __ args
#             ____.i.. _ a.. 0
#             s__. - $
#         ____
#             s__. - ____.i..
#
#         __ u.. __ no. N..
#             ____.u.. _ u...
#
# '''
# And we can use this exception quite easily:
# '''
#
# ___
#     r___ A..
# _____ A.. __ ex
#     print re.. ?
#     print ?.u..
#
# '''
# Or with a custom (internal) message:
# '''
#
# ___
#     r___ A..('custom message...', 10, 20)
# _____ A.. __ ex
#     print re.. ?
#
# '''
# And of course, the user message can be customized too:
# '''
#
# ___
#     r___ A..('custom message...', 10, 20, user_err_msg='custom user message')
# _____ A.. __ ex
#     print re.. ?
#     print ?.u..
#
# '''
# While we're at it, we know that we'll need to r_ the same JSON format when an exception occurs - so let's write it
# into our base exception class:
# '''
#
# _______ j..
#
# c_ APIException E..
#     """Base API exception"""
#
#     http_status = HT...I_S_E
#     internal_err_msg = 'API exception occurred.'
#     user_err_msg = "We are sorry. An unexpected error occurred on our end."
#
#     ___ - ____ @ user_err_msg _ N..
#         __ args
#             ____.i.. _ a.. 0
#             s___. - $
#         ____
#             s__. - ____.i..
#
#         __ u.. __ no. N..
#             ____.u.. _ u..
#
#     ___ to_json ____
#         err_object = 'status': ____.h_s, 'message': ____.u..
#         r_ ____.d.. ?
#
# '''
# Now we can easily use this base class, and get consistent results:
# '''
#
# ___
#     r___ A..
# _____ A.. __ ex
#     print re.. ? ?.to_
#
# '''
# And because we'll want to log exceptions, let's also write a logger directly into our base class:
# '''
#
# ____ d.t. _______ d_t_
#
# c_ APIException E..
#     """Base API exception"""
#
#     http_status = HT__.I_S_E
#     internal_err_msg = 'API exception occurred.'
#     user_err_msg = "We are sorry. An unexpected error occurred on our end."
#
#     ___ - ____ $ user_err_msg _ N..
#         __ args
#             ____.i.. _ a.. 0
#             s__. - $
#         ____
#             s__. - ____.i..
#
#         __ u.. __ no. N..
#             ____.u.. _ u..
#
#     ___ to_json ____
#         err_object _ 'status': ____.h.. 'message': ____.u..
#         r_ ____.d.. ?
#
#     ___ log_exception ____
#         exception _ {
#             "type": ty.. ____. -n
#             "http_status": ____.h..
#             "message": ____.a. 0 __ ____.a.. ____ ____.i..
#             "args": ____.a.. 1
#         }
#         print_*EXCEPTION: |d_t_.u.n_.i_f.|: |?
#
# ___
#     r___ A..
# _____ A.. __ ex
#     ?.l..
#     print ?.to_
#
# '''
# Now let's finish up our hierarchy:
# '''
#
# c_ ApplicationException A..
#     """Indicates an application error (not user caused) - 5xx HTTP type errors"""
#     http_status = HT__.I_S_E
#     internal_err_msg = "Generic server side exception."
#     user_err_msg = "We are sorry. An unexpected error occurred on our end."
#
# c_ DBException A..
#     """General database exception"""
#     http_status = HT__.I_S_E
#     internal_err_msg = "Database exception."
#     user_err_msg = "We are sorry. An unexpected error occurred on our end."
#
# c_ DBConnectionError D..
#     """Indicates an error connecting to database"""
#     http_status = HT__.I_S_E
#     internal_err_msg = "DB connection error."
#     user_err_msg = "We are sorry. An unexpected error occurred on our end."
#
# c_ ClientException A..
#     """Indicates exception that was caused by user, not an internal error"""
#     http_status = HT_.B_R
#     internal_err_msg = "Client submitted bad request."
#     user_err_msg = "A bad request was received."
#
# c_ NotFoundError C..
#     """Indicates resource was not found"""
#     http_status = HT__.N_F
#     internal_err_msg = "Resource was not found."
#     user_err_msg = "Requested resource was not found."
#
# c_ NotAuthorizedError C..
#     """User is not authorized to perform requested action on resource"""
#     http_status = HT__.UN..
#     internal_err_msg = "Client not authorized to perform operation."
#     user_err_msg = "You are not authorized to perform this request."
#
# '''
# Also, since we have a but more functionality available to us with our exceptions, let's refine the function that raises
# these exceptions:
# '''
#
# ___ lookup_account_by_id account_id
#     # mock of various exceptions that could be raised getting an account from database
#     __ no. isi.. ?, in. or ? <_ 0
#         r___ C.. _*Account number |?| is invalid.',
#                               _*? = |?|',
#                               'type error - account number not an integer')
#
#     __ ? < 100
#         r___ D.. 'Permanent failure connecting to database.', 'db=db01'
#     ____ ? < 200
#         r___ N..  User does not have permissions to read this account', _*?=|?|
#     ____ ? < 300
#         r___ N.. _*Account not found.', _*?=|?
#     ____
#         r_ A.. ? 'Savings'
#
# '''
# Now we can re-write our API endpoint and very easily handle those exceptions:
# '''
#
# ___ get_account account_id
#     ___
#         account = l.. ?
#     _____ A.. __ ex
#         ?.l..
#         r_ ?.to_
#     ____:
#         r_ HT__.O. |"id": a__.? "type": a__.a_t
#
# get_account('ABC')
# get_account(50)
# get_account(150)
# get_account(250)
# get_account(350)
#
# '''
# #### Inheriting from Multiple Exceptions
# We haven't covered multiple inheritance yet, but Python supports it, and it is very easy to use to solve a specific
# problem we may encounter with exceptions, so i want to mention it here.
# Although we may want to raise a custom exception for some specific error, sometimes we may be wondering whether
# to raise a built-in exception that would work just as well, or raise a custom exception.
# Here's an example of where this might occur:
# Suppose we have a custom exception we use to tell a user of our function/library that the value they provided to some
# function is not the right value - maybe it needs to be a integer greater than or equal to 0.
# We might have a custom exception just for that - remember what we discussed earlier, we might want our application to
# raise custom exceptions for everything, based off some application base exception our users could broadly trap.
# '''
#
# c_ AppException E..
#     """generic application exception"""
#
# c_ NegativeIntegerError A..
#     """Used to indicate an error when an integer is negative."""
#
# ___ set_age age
#     __ ? < 0
#         r___ N.. age cannot be negative
#
# ___
#     set_age(-10)
# _____ N.. __ ex
#     print re.. ?
#
#
# '''
# But the problem is that this is also a `ValueError`, and our users may want to trap it as a `ValueError` for some
# reason, not a `NegativeIntegerError` (or `AppException` as is possible here).
# The beauty of multiple inheritance is that we can have our custom exception inherit from **more than one** exception.
# All we need to understand here, is that if we inherit from more than one class, then our subclass is considered
# a subclass of **both** parents.
# '''
#
# c_ BaseClass1
#     p..
#
# c_ BaseClass2
#     p..
#
# c_ MyClass B1 B2
#     p..
#
# iss.. M.. B1
# iss.. M.. B2
#
# '''
# So, we can do the same thing with our exception:
# '''
#
# c_ NegativeIntegerError A.. V..
#     """Used to indicate an error when an integer is negative."""
#
# '''
# Now this exception is a subclass of **both** `AppException` and `ValueError`:
# '''
#
# iss.. N.. A..
# iss.. N.. V..
#
# '''
# And we can trap it with either of those exception types:
# '''
#
# ___ set_age age
#     __ ? < 0
#         r___ N.. age cannot be negative
#
# ___
#     set_age(-10)
# _____ N.. __ ex
#     print re.. ?
#
# ___
#     set_age(-10)
# _____ V.. __ ex
#     print re.. ?
#
# '''
# So this solves the problem - deciding between a custom exception vs a standard exception - we can just use both
# (or more!)
# '''
