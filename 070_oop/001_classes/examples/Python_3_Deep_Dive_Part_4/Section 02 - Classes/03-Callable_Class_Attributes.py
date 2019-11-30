# %%
'''
### Callable Class Attributes
'''

# %%
'''
Class attributes can be any object type, including callables such as functions:
'''

# %%
class Program:
    language = 'Python'
    
    def say_hello():
        print(f'Hello from {Program.language}!')

# %%
print(Program.__dict__)
#
# # %%
# '''
# As we can see, the `say_hello` symbol is in the class dictionary.
# We can also retrieve it using either `getattr` or dotted notation:
# '''
#
# # %%
print(Program.say_hello, getattr(Program, 'say_hello'))
#
# # %%
# '''
# And of course we can call it, since it is a callable:
# '''
#
# # %%
Program.say_hello()
#
# # %%
# getattr(Program, 'say_hello')()
#
# # %%
# '''
# We can even access it via the namespace dictionary as well:
# '''
#
# # %%
print(Program.__dict__['say_hello'])
#
# # %%
