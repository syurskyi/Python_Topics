# The try_finally Statement
try:
    <statements>               # Run this action first
finally:
    <statements>               # Always run this code on the way out


# Unified try_except_finally
try:                               # Merged form
    main-action
except Exception1:
    handler1
except Exception2:
    handler2
...
else:
    else-block
finally:
    finally-block

# Unified try Statement Syntax
try:                               # Format 1
    statements
except [type [as value]]:          # [type [, value]] in Python 2
    statements
[except [type [as value]]:
    statements]*
[else:
    statements]
[finally:
    statements]

try:                               # Format 2
    statements
finally:
    statements

# Combining finally and except by Nesting
try:                               # Nested equivalent to merged form
    try:
        main-action
    except Exception1:
        handler1
    except Exception2:
        handler2
    ...
    else:
        no-error
finally:
    cleanup
