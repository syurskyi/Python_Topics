# 
# # Class decorator to trace external instance attribute fetches
# 
# ___ Tracer aClass                                   # On @decorator
#     c_ Wrapper
#         ___ -  ____, $ $$           # On instance creation
#             ____.wrapped _ aClass $ $$     # Use enclosing scope name
#         ___ -g ____ attrname
#             print('Trace:', a...                # Catches all but .wrapped
#             r_ g... ____.wr... a..    # Delegate to wrapped object
#     r_ W...
# 
# _T..
# c_ Person                                         # Person = Tracer(Person)
#     ___ - ____ name hours rate            # Wrapper remembers Person
#         ____.n.. _ n...
#         ____.h.. _ h...
#         ____.r.. _ r...                              # In-method fetch not traced
#     ___ pay ____
#         r_ ____.h.. * ____.r..
# 
# bob _ P__('Bob', 40, 50)                           # bob is really a Wrapper
# print(?.n..                                       # Wrapper embeds a Person
# print(?.p..                                      # Triggers -g 
# 
# 
# 
# 
# # Manage instances like the prior example, but with a metaclass
# 
# ___ Tracer classname supers classdict             # On class creation call
#     aClass _ ty.. c.. s... cl..       # Make client class
#     c_ Wrapper
#         ___ - ____ $ $$           # On instance creation
#             ____.wrapped _ a... $ $$
#         ___ -g  ____ attrname
#             print('Trace:', a..                # Catches all but .wrapped
#             r_ g ____.wr.. a..    # Delegate to wrapped object
#     r_ W..
# 
# c_ Person m.._T..                       # Make Person with Tracer
#     ___ - ____ name hours rate            # Wrapper remembers Person
#         ____.n.. _ n..
#         ____.h.. _ h..
#         ____.r.. _ r..                              # In-method fetch not traced
#     ___ pay ____
#         r_ ____.h.. * ____.r..
# 
# bob _ P.. 'Bob', 40, 50                          # bob is really a Wrapper
# print(?.n..                                       # Wrapper embeds a Person
# print(?.p..                                      # Triggers -g 
# 
