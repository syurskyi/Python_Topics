# c_ Tracer
#     ___ - ____ aClass               # On @decorator
#         ____.aClass _ a...                  # Use instance attribute
# 
#     ___ -c ____ $                # On instance creation
#         ____.wrapped _ ____.aClass($     # ONE (LAST) INSTANCE PER CLASS!
#         r_ ____
# 
#     ___ __getattr__(____, attrname):
#         print('Trace: ' + attrname)
#         r_ getattr(____.wrapped, attrname)
# 
# 
# _T..                                      # Triggers __init__
# c_ Spam                                   # Like: Spam = Tracer(Spam)
#     ___ display ____
#         print('Spam!' * 8)
# 
# 
# food = Spam()                                 # Triggers __call__
# food.display()                                # Triggers __getattr__
# 
# 
# _T..
# c_ Person:                                 # Person = Tracer(Person)
#     ___ - ____ name                 # Wrapper bound to Person
#         ____.n.. _ n..
# 
# 
# bob = Person('Bob')                           # bob is really a Wrapper
# print(bob.name)                               # Wrapper embeds a Person
# sue = Person('Sue')
# print(sue.name)                               # sue overwrites bob
# print(bob.name)                               # OOPS: now bob's name is 'Sue'!
# 
