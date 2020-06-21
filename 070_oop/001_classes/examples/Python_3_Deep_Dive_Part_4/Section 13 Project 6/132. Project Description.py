# %%
'''
### Project 6 - Exceptions
'''

# %%
'''
Suppose we have a Widget online sales application and we are writing the backend for it. We want a base 
`WidgetException` class that we will use as the base class for all our custom exceptions we raise from our Widget 
application.
'''

# %%
'''
Furthermore we have determined that we will need the following categories of exceptions:
'''

# %%
'''
```
1. Supplier exceptions
    a. Not manufactured anymore
    b. Production delayed
    c. Shipping delayed
    
2. Checkout exceptions
    a. Inventory type exceptions
        - out of stock
    b. Pricing exceptions
        - invalid coupon code
        - cannot stack coupons
```
'''

# %%
'''
Write an exception class hierarchy to capture this. In addition, we would like to implement the following functionality:
* implement separate internal error message and user error message
* implement an http status code associated to each exception type (keep it simple, use a 500 (server error) error 
for everything except invalid coupon code, and cannot stack coupons, these can be 400 (bad request)
* implement a logging function that can be called to log the exception details, time it occurred, etc.
* implement a function that can be called to produce a json string containing the exception details you want to display 
to your user (include http status code (e.g. 400), the user error message, etc)
'''

# %%
'''
##### Bonus
'''

# %%
'''
Log the traceback too - you'll have to do a bit of research for that! 
I'm going to use the `TracebackException` class in the `traceback` module:
https://docs.python.org/3/library/traceback.html#tracebackexception-objects
'''

# %%
'''
In particular, look at the class method `from_exception` (and remember that inside your exception class, the exception 
will be `self`!) and the `format` instance method. That method returns a generator, so you'll need to `list` it to print 
out everything in that traceback.
'''

# %%
'''
Good luck!
'''

# %%
