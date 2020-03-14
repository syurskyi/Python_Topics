# Alternate formulation using function attributes directly

from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.log.log(wrapper.level, wrapper.logmsg)
            return func(*args, **kwargs)

        # Attach adjustable attributes
        wrapper.level = level
        wrapper.logmsg = logmsg
        wrapper.log = log

        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    print(add(2, 3))

    # Change the log message
    add.logmsg = 'Add called'
    print(add(2, 3))

    # Change the log level
    add.level = logging.WARNING
    print(add(2, 3))

# Discussion
# The key to this recipe lies in the accessor functions [e.g., set_message() and set_lev
# el()] that get attached to the wrapper as attributes. Each of these accessors allows internal
# parameters to be adjusted through the use of nonlocal assignments.
# An amazing feature of this recipe is that the accessor functions will propagate through
# multiple levels of decoration (if all of your decorators utilize @functools.wraps). For
# example, suppose you introduced an additional decorator, such as the @timethis decorator
# from Recipe 9.2, and wrote code like this:

# One extremely subtle facet of this recipe is the choice to use accessor functions in the
# first place. For example, you might consider an alternative formulation solely based on
# direct access to function attributes like this:
# This approach would work to a point, but only if it was the topmost decorator. If you
# had another decorator applied on top (such as the @timethis example), it would shadow
# the underlying attributes and make them unavailable for modification. The use of accessor
# functions avoids this limitation.
# Last, but not least, the solution shown in this recipe might be a possible alternative for
# decorators defined as classes, as shown in Recipe 9.9.

