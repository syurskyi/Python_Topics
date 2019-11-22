
# Sending Exceptions to Generators
# In fact we can also raise any exception inside a generator by using the throw() method

def gen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('exception must have happened...')

g = gen()
next(g)
g.send('hello')g.throw(ValueError, 'custom message')

# Sending Exceptions to Generators
# As you can see, the exception occurred inside the generator, and then propagated up to the caller
# (we did not intercept and silence the exception). Of course we can do that if we want to:

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError:
        print('received the value error...')
    finally:
        print('generator exiting and closing')

g = gen()
next(g)
g.send('hello')
g.throw(ValueError, 'stop it!')

# Sending Exceptions to Generators
#
# if the generator catches the exception and yields a value, that is the return value of the throw() method
#
# And the generator is now in a suspended state, waiting for our next call:

from inspect import getgeneratorstate

def gen():
    while True:
        try:
            received = yield
            print(received)
        except ValueError as ex:
            print('ValueError received...', ex)

g = gen()
next(g)
g.send('hello')
g.throw(ValueError, 'custom message')
g.send('hello')
getgeneratorstate(g)


# Sending Exceptions to Generators
#
# if the generator does not catch the exception, the exception is propagated back to the caller
#
# And the generator is now in a closed state:

def gen():
    while True:
        received = yield
        print(received)

g = gen()
next(g)
g.send('hello')


# Sending Exceptions to Generators
#
# if the generator catches the exception, and exits (returns), the StopIteration exception is propagated to the caller

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as ex:
        print('ValueError received', ex)
        return None

g = gen()
next(g)
g.send('hello')

g.throw(ValueError, 'custom message')

# Sending Exceptions to Generators
#
# if the generator catches the exception, and raises another exception, that exception is propagated to the caller
#
# And out generator is, once again, in a closed state:

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as ex:
        print('ValueError received...', ex)
        raise ZeroDivisionError('not really...')

g = gen()
next(g)
g.send('hello')

g.throw(ValueError, 'custom message')

getgeneratorstate(g)

# Sending Exceptions to Generators
#
# As you can see our traceback includes both the ZeroDivisionError and the ValueError that caused the ZeroDivisionError
# to happen in the first place. If you don't want to have that traceback you can easily remove it and only display
# the ZeroDivisionError (I will cover this and exceptions in detail in a later part of this series):

def gen():
    try:
        while True:
            received = yield
            print(received)
    except ValueError as ex:
        print('ValueError received...', ex)
        raise ZeroDivisionError('not really...') from None

g = gen()
next(g)
g.send('hello')

g.throw(ValueError, 'custom message')

# Sending Exceptions to Generators
#
# Suppose we have a coroutine that handles writing data to a database. We have seen in some previous examples where
# we could use a coroutine to start and either commit or abort a transaction - based on closing the generator or
# forcing an exception to happen in the body of the generator.
#
# Let's revisit this example, but now we'll want to use exceptions to indicate to our generator whether to commit or
# abort a transaction, without necessarily exiting the generator:

class CommitException(Exception):
    pass

class RollbackException(Exception):
    pass

def write_to_db():
    print('opening database connection...')
    print('start transaction...')
    try:
        while True:
            try:
                data = yield
                print('writing data to database...', data)
            except CommitException:
                print('committing transaction...')
                print('opening next transaction...')
            except RollbackException:
                print('aborting transaction...')
                print('opening next transaction...')
    finally:
        print('generator closing...')
        print('aborting transaction...')
        print('closing database connection...')

sql = write_to_db()
next(sql)
sql.send(100)
sql.throw(CommitException)
sql.send(200)
sql.throw(RollbackException)
sql.send(200)
sql.throw(CommitException)
sql.close()

# Sending Exceptions to Generators
#
# throw() and close()
#
# The close() method does essentially the same thing as throw(GeneratorExit) except that when that exception is thrown
# using throw(), Python does not silence the exception for the caller:

def gen():
    try:
        while True:
            received = yield
            print(received)
    finally:
        print('closing down...')

g = gen()
next(g)
g.send('hello')
g.close()

g = gen()
next(g)
g.send('hello')
g.throw(GeneratorExit)

# Sending Exceptions to Generators
# throw() and close()
# Even if we catch the exception, we are still exiting the generator, so using throw will result in the caller
# receiving a StopIteration exception.
#
# So, we can use throw to close the generator, but as the caller we now have to handle the exception that
# propagates up to us:

def gen():
    try:
        while True:
            received = yield
            print(received)
    except GeneratorExit:
        print('received generator exit...')
    finally:
        print('closing down...')

g = gen()
next(g)
g.close()

g = gen()
next(g)
g.throw(GeneratorExit)

g = gen()
next(g)
try:
    g.throw(GeneratorExit)
except StopIteration:
    print('silencing GeneratorExit...')
    pass
