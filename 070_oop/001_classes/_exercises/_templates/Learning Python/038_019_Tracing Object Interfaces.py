# c_ Wrapper:
#     ___ - ____, object
#         ____.wrapped = obj..                   # Save object
#     ___ -g ____ attrname
#         print('Trace:', a..                # Trace fetch
#         r_ ge... ____.wr... a...   # Delegate fetch
# 
# x = ? ([1,2,3])                         # Wrap a list
# ?.ap.. 4                                  # Delegate to list method
# # Trace: append
# x.wrapped                                    # Print my member
# # [1, 2, 3, 4]
# 
# x = ? "a" 1, "b" 2                # Wrap a dictionary
# li. ?.k..                               # Delegate to dictionary method
# # Trace: keys                                      # Use list() in 3.0
# # ['a', 'b']
# 
# 
# ___ Tracer aClass                                   # On @decorator
#     c_ Wrapper
#         ___ - ____, $ $$:           # On instance creation
#             ____.fetches _ 0
#             ____.wrapped _ aClass $ $$     # Use enclosing scope name
#         ___ -g ____ attrname
#             print('Trace: ' + a...               # Catches all but own attrs
#             ____.f.. += 1
#             r_ -g ____.wrapped, a..    # Delegate to wrapped obj
#     r_ W..
# 
# _T
# c_ Spam:                                    # Spam = Tracer(Spam)
#     ___ display ____                         # Spam is rebound to Wrapper
#         print('Spam!' * 8)
# 
# _T..
# c_ Person:                                  # Person = Tracer(Person)
#     ___ - ____ name hours rate     # Wrapper remembers Person
#         ____.n... _ n..
#         ____.h.. _ h..
#         ____.r.. _ r..
#     ___ pay ____                             # Accesses outside class traced
#         r_ ____.h.. * ____.r..          # In-method accesses not traced
# 
# food = Spam()                                  # Triggers Wrapper()
# food.display()                                 # Triggers __getattr__
# print([food.fetches])
# 
# bob = Person('Bob', 40, 50)                    # bob is really a Wrapper
# print(bob.name)                                # Wrapper embeds a Person
# print(bob.pay())
# 
# print('')
# sue = Person('Sue', rate=100, hours=60)        # sue is a different Wrapper
# print(sue.name)                                # with a different Person
# print(sue.pay())
# 
# print(bob.name)                                # bob has different state
# print(bob.pay())
# print([bob.fetches, sue.fetches])              # Wrapper attrs not traced
# 
# 
# from tracer import Tracer     # Decorator moved to a module file
# 
# _T..
# c_ MyList li.. p..      # MyList = Tracer(MyList)
# 
# 
# x = MyList([1, 2, 3])         # Triggers Wrapper()
# x.append(4)                   # Triggers __getattr__, append
# # Trace: append
# x.wrapped
# # [1, 2, 3, 4]
# 
# WrapList = Tracer(list)       # Or perform decoration manually
# x = WrapList([4, 5, 6])       # Else subclass statement required
# x.append(7)
# # Trace: append
# x.wrapped
# # [4, 5, 6, 7]
# 
# 
# _T..                                         # Decorator approach
# c_ Person: ...
# bob = Person('Bob', 40, 50)
# sue = Person('Sue', rate=100, hours=60)
# 
# 
# c_ Person: ...                                # Non-decorator approach
# bob = W.. P..('Bob', 40, 50))
# sue = W.. P..('Sue', rate=100, hours=60))
