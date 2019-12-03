# The try_exceptelse Statement
# NOTE: the first few snippets from this chapter are not runnable code,
# but are included in case you wish to expand them into working examples.


try:
    <statements>            # Run this main action first
except <name1>:
    <statements>            # Run if name1 is raised during try block
except (name2, name3):
    <statements>            # Run if any of these exceptions occur
except <name4> as <data>:
    <statements>            # Run if name4 is raised, and get instance raised
except:
    <statements>            # Run for all (other) exceptions raised
else:
    <statements>            # Run if no exception was raised during try block

# Catching any and all exceptions
try:
    action()
except NameError:
    ...
except IndexError:
    ...
except KeyError:
    ...
except (AttributeError, TypeError, SyntaxError):
    ...
else:
    ...

# Catching all_ The empty except and Exception
try:
    action()
except NameError:
    ...                   # Handle NameError
except IndexError:
    ...                   # Handle IndexError
except:
    ...                   # Handle all other exceptions
else:
    ...                   # Handle the no-exception case


try:
    action()
except:
    ...                   # Catch all possible exceptions


try:
    action()
except Exception:
    ...                   # Catch all possible exceptions, except exits
