# Function
# Python Scope Basics

# X = 99
#
# ___ func
#     X = 88
#
# # Global scope
# X = 99  # X and func assigned in module: global
#
# ___ func  # Y and Z assigned in function: locals
#     # Local scope
#     Z = X + Y  # X is a global
#     ___ Z
#
# print(f_(1))  # func in module: result=100
#
# print()
# ######################################################################################################################
# The global Statement

# X = 88  # Global X
#
# ___ func
#     g_ X
#     X = 99  # Global X: outside def
#
# func()
# print(X)  # Prints 99
#
# y, z = 1, 2  # Global variables in module
#
# ___ all_global
#     g___ x  # Declare globals assigned
#     x = y + z  # No need to declare y, z: LEGB rule
#
# print()
# ######################################################################################################################
# Scopes and Nested Functions

# X = 99  # Global scope name: not used
# print(X)
#
# ___ f1
#     X = 88  # Enclosing def local
#
#     ___ f2
#         print(X)  # Reference made in nested def
#
#     f2()
#
# f1()  # Prints 88: enclosing def local
#
# ___ f1
#     X = 89
#
#     ___ f2
#         print(X)  # Remembers X in enclosing def scope
#
#     ___ f2  # Return f2 but don't call it
#
#
# action = f1()  # Make, return function
# action()  # Call it now: prints 88
#
# print()
# ######################################################################################################################
# Retaining Enclosing Scope State with Defaults

# ___ f1
#     x = 88
#
#     ___ f2_x_x  # Remember enclosing scope X with defaults
#         print(x)
#
#     f2()
#
# f1()  # Prints 88
#
#
# ___ f1
#     x = 88  # Pass x along instead of nesting
#     f2(x)  # Forward reference okay
#
# ___ f2 x
#     print(x)
#
# f1()

# print()
# ######################################################################################################################
# Nested scopes, defaults, and lambdas

# ___ func
#     x = 4
#     action = l_ n x ** n  # x remembered from enclosing def
#     ___ a_
#
# x f_
# print(x(2))  # Prints 16, 4 ** 2
#
# ___ func
#     x = 4
#     action = l_ n x_x x ** n  # Pass x in manually
#     ___ a_

# print()
# ######################################################################################################################
# nonlocal in Action

# ___ tester start
#     state = start  # Referencing nonlocals works normally

    # ___ nested label
    #     print l_, s_)  # Remembers state in enclosing scope
    # ___ n_

# F = t_(0)
# F('spam')
# F('ham')

# ___ tester start
#     state = start

    # ___ nested label
    #     print l_ s_
    #     s_ += 1  # Cannot change by default (or in 2.6)

    # ___ n_

# F = t_(0)
# F('spam')  # UnboundLocalError: local variable 'state' referenced before assignment

# print()
# ######################################################################################################################
# Using nonlocal for changes

# ___ tester start
#     state = start  # Each call gets its own state

    # ___ nested label
    #     n______
    #     s___  # Remembers state in enclosing scope
    #     print(l_, s_)
    #     s_ __ 1  # Allowed to change it if nonlocal
    # ____ n_

# F = t_(0)

# print('#' * 52 + ' Increments state on each call')
# F('spam')  # Increments state on each call
# F('ham')
# F('eggs')

# print('#' * 52 + ' Make a new tester that starts at 42')
# G = t__42  # Make a new tester that starts at 42
# G__spam

# print('#' * 52 + ' My state information updated to 43')
# G__eggs  # My state information updated to 43

# print('#' * 52 + ' ')
# F__bacon  # But F's is where it left off: at 3
# Each call has different state information

# print()
# ######################################################################################################################
# Arguments and Shared References

# ___ f_a_  # a is assigned to (references) passed object
#     a = 99  # Changes local variable a only

# b = 88
# f(b)  # a and b both reference same 88 initially
# print(b)  # b is not changed

# ___ changer a b  # Arguments assigned references to objects
#     a = 2  # Changes local name's value only
    # b_0_  'spam'  # Changes shared object in-place

# X = 1
# L = [1, 2]  # Caller
# c_(X, L)  # Pass immutable and mutable objects
# X, L  # X is unchanged, L is different!

# X = 1
# a = X  # They share the same object
# a = 2  # Resets 'a' only, 'X' is still 1
# print(X)

# L = [1, 2]
# b = L  # They share the same object
# b_0_ _ 'spam'  # In-place change: 'L' sees the change too
# print(L)

# print()

# ######################################################################################################################
# suppose we have points (represented as tuples), and we want to sort them based on the distance of the point from
# some other fixed point:

# origin = (0, 0)
# l = [(1,1), (0, 2), (-3, 2), (0,0), (10, 10)]
# dist2 = l_ x_ y| (x|0|-y|0|)**2 + (x|1|-y|1|)**2
# dist2((0,0), (1,1))
# s_(l, key _ l_ x| dist2((0,0)_ x))
# s_(l, key_p_(dist2, (0,0)))
#
# print()
# ######################################################################################################################
#  we have some generic email() function that can be used to notify someone when various things happen
#  in our application. But depending on what is happening we may want to notify different people.

# ___ sendmail to subject body
#     # code to send email
#     print('To:|0|, Subject:|1|, Body:|2|'.f_ to subject body
#
# # Now, we may haver different email adresses we want to send notifications to, maybe defined in a config file in our app.
# # Here, I'll just use hardcoded variables:
#
# email_admin = 'palin@python.edu'
# email_devteam = 'idle@python.edu;cleese@python.edu'
#
# # Now when we want to send emails we would have to write things like:
#
# sendmail(email_admin, 'My App Notification', 'the parrot is dead.')
# sendmail(';'.j_ email_admin email_devteam _ 'My App Notification', 'the ministry is closed until further notice.')
#
# # We could simply our life a little using partials this way:
#
# send_admin = p_(sendmail, email_admin, 'For you eyes only')
# send_dev = p_(sendmail, email_devteam, 'Dear IT:')
# send_all = p_(sendmail, ';'.j_((email_admin, email_devteam)), 'Loyal Subjects')
#
# send_admin('the parrot is dead.')
# send_all('the ministry is closed until further notice.')
#
# # Finally, let's make this a little more complex, with a mixture of positional and keyword-only argument
#
# print()
# ######################################################################################################################
# Functions defined inside anther function can reference variables from that enclosing scope,
# just like functions can reference variables from the global scope.

# ___ outer_func
#     x _ 'hello'
#
#     ___ inner_func
#         print(x)
#
#     inner_func()
#
# outer_func()
#
# print()
# ######################################################################################################################
# if we assign a value to a variable, it is considered part of the local scope, and potentially masks enclsogin scope
# variable names:
#
# x _ 'hello'
# ___ inner
#     no_ x
#     x _ python'
# inner()
# print(x)
#
# outer()

# Of course, this can work at any level as well:

# ___ outer
#     x _ 'hello'
#
#     ___ inner1
#         ___ inner2
#             no_
#             x
#             x _ 'python'
#
#         inner2
#
#     inner1
#     print x
#
# outer()
#
# print()
# ######################################################################################################################
# Let's examine that concept of a cell to create an indirect reference for variables that are in multiple scopes.

# ___ outer
#     x _ 'python'
#     ___ inner
#         print x
#     r_ inn_
#
# fn _ out___
# fn.__c_.c_f_
# fn.__c_
#
# print()
# ######################################################################################################################
# Modifying the Free Variable
# We know we can modify nonlocal variables by using the nonlocal keyword. So the following will work:

# ___ counter
#     count _ 0  # local variable
#
#     ___ inc
#         no_
#         co____  # this is the count variable in counter
#         co___ += 1
#         r_ co___
#
#     r_ inc
#
# c = co____
# c()
# c()
#
# print()
# ######################################################################################################################
# Shared Extended Scopes
#
# ___ outer
#     count _ 0
#
#     ___ inc1
#         no__
#         co__
#         co__ += 1
#         r_ co__
#
#     ___ inc2
#         no__
#         co__
#         co__ += 1
#         r_ co__
#
#     r_ inc1 inc2
#
# fn1, fn2 = outer()
# fn1.__c_, fn2.__c_
#
# # As you can see here, the count label points to the same cell.
#
# fn1()
# fn1()
# fn2()
#
# print()