# # %%
# '''
# ### Property Decorators
# '''
#
# # %%
# '''
# As I explain in the lecture video, the `property` callable actually returns itself:
# '''
#
# # %%
# p = p....(fget=l____ ____: print('getting property'))
#
# # %%
# p
#
# # %%
# '''
# As you can see `p` is a property, and in fact is the same property that was created.
# '''
#
# # %%
# '''
# Think back to how decorators work:
# '''
#
# # %%
# ___ my_decorator fn
#     print('decorating function')
#     ___ inner 0a.. 00k..
#         print('running decorated function')
#         r_ fn 0a.. 00k..
#     r_ i..
#
# # %%
# ___ undecorated_function a, b
#     print('running original function')
#     r_ a + b
#
# # %%
# '''
# Now we can decorate our undecorated function this way:
# '''
#
# # %%
# decorated_func _ my.. u..
#
# # %%
# '''
# And we can call the decorated function:
# '''
#
# # %%
# d... 10 20
#
# # %%
# '''
# Now instead of giving the decorate function a new symbol, we could have just re-used the same symbol:
# '''
#
# # %%
# ___ my_func a b
#     print('running original function')
#     r_ a + b
#
# my_func _ m._d. my..
#
# # %%
# ? 10 20
#
# # %%
# '''
# And of course this is exactly what the decorator `@` syntax does:
# '''
#
# # %%
# 0m..
# ___ my_func a b
#     print('running original function')
#     r_ a + b
#
# # %%
# ?  10 20
#
# # %%
# '''
# Ok, now that we've refreshed our memory on decorators, we should be ready to look at the `property` callable.
# The `property` callable creates a property object, **and returns it**.
# In other words, we could create our property this way, as usual:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____._na.. _ n...
#
#     ___ n... ____
#         r_ ____._n..
#
#     n... _ p.... n...
#
# # %%
# p _ ? Alex
#
# ?.n...
#
# # %%
# '''
# But you'll notice that line: `name = property(name)` - that's exactly what the decorator syntax does for us!
# So instead we can write:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____._na.. _ n...
#
#     0p....
#     ___ n... ____
#         r_ ____._na..
#
# # %%
# p _ ? Guido
# print ?.n...
#
# # %%
# '''
# If you refresh your memory on the single dispatch generic function decorator, you'll remember that the decorated
# function included another property, the `register` property that was itself a decorator.
# Well, the `property` object has some properties, like `setter` that will basically accept a reference to the setter
# method, and return itself also.
# '''
#
# # %%
# p _ p.... l____ ____ 'getter'
#
# # %%
# dir(p)
#
# # %%
# '''
# So, we can "register" and setter method, using the `setter` callable, and get our property back as well:
# '''
#
# # %%
# p
#
# # %%
# p2 _ p.s... l____ ____ 'setter'
#
# # %%
# id(p), id(p2)
#
# # %%
# '''
# Now you'll notice that the property id has changed. The setter callable actually creates a new property
# (with both the original getter, and the new setter assigned).
# But that does not really matter, we just have a new property object that we can use to assign to a symbol -
# and that property will have both the getter and the setter defined.
# Let's do this manually (without the decorator syntax first):
# '''
#
# # %%
# c_ Person
#     ___ - ____  name
#         ____._na.. _ n...
#
#     ___ n... ____
#         r_ ____._na..
#
#     n... _ p.... n...
#
#     # creating another symbol that holds on to
#     # the name property
#     name_prop _ n...
#
#     # because herte I'm redefining name, so we lose
#     # our original reference to the property object
#     ___ n... ____ value
#         ____._na.. _ v..
#
#     n... _ n.._p_.s... n...
#
#     # finally delete name_prop which we no longer need
#     de. n._p.
#
# # %%
# print ?.-d
#
# # %%
# '''
# And we now have a `name` property that we created in two steps: first create the property with just a getter.
# Then we replaced our property with a new property that had both the getter and the setter.
# '''
#
# # %%
# p _ ? Alex
# print ?.n...
#
# # %%
# ?.n... _ 'Raymond'
# print ?.n...
#
# # %%
# '''
# Hopefully you can now see where the original property (with just the getter), had a callable `setter` that "added"
# the setter to the property (by creating a new property with both getter and setter), that also returned the (new)
# property object.
# So, we can simplify our code this way:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____._na.. _ n...
#
#     0p....
#     ___ n... ____
#         r_ ____._na..
#
#     # what's the property name now? --> name
#     # so name has a setter callable
#     0n....s...
#     ___ n... ____ v..
#         ____._na.. _ v..
#
# # %%
# '''
# Note that if we had not named our setter function `name` the property name would have changed!
# Remember that:
# ```
# @dec
# def my_func():
#     pass
#  ```
#  returns a decorated function with the same name as the original function
# '''
#
# # %%
# print ?.-d
#
# # %%
# p _ ? Alex
#
# # %%
# print ?.n...
#
# # %%
# ?.n... _ Guido
# print ?.n...
#
# # %%
# '''
# Just to show you, if we had not used the same name for the setter function:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____._na.. _ n...
#
#     0p....
#     ___ n... ____
#         r_ ____._na..
#
#     # p.... is now called name
#
#     0n....s...
#     ___ full_name ____ v..
#         ____._na.. _ v..
#
# # %%
# print ?.-d
#
# # %%
# '''
# As you can see we now have two properties on the class! The first one `name` will only work as a getter.
# And the second one `full_name` will work as both a getter and a setter:
# '''
#
# # %%
# p _ ? Alex
#
# # %%
# print ?.n...
#
# # %%
# print ?.f.._n..
#
# # %%
# ?.f.._n.. _ Raymond
#
# # %%
# print ?.f.._n.
#
# # %%
# '''
# But this won't work:
# '''
#
# # %%
# t___
#     ?.n... _  Guido
# e_ A... a_ ex:
#     print ?
#
# # %%
# '''
# Technically, the property callable has both a getter and setter method - so we can create the setter first,
# then "add in" the getter. But since the first argument to `property` is the getter, we have to work a bit more to do it:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____._na.. _ n...
#
#     n... _ p....  # an "empty" prroperty - no getter or setter
#
#     0n....s...
#     ___ n... ____ value
#         ____._name _ v...
#
# # %%
# '''
# By the way, we now have a property that can be set, but not read back!
# '''
#
# # %%
# p _ ? Alex
#
# # %%
# print ?.-d
#
# # %%
# ?.n... _ 'Raymond'
#
# # %%
# print ?.-d
#
# # %%
# t__
#     p.n...
# e__ A... a_ ex
#     print ?
#
# # %%
# '''
# So, if you ever need an attribute that is "write-only" - you can do it. Maybe the data is sensitive, and you want
# to set it, but not show back to users... But the data is never truly private, so at best you're obfuscating the data -
# so in my experience I've never had to do something like that. Just wanted you to see this in case the need ever came up.
# '''
#
# # %%
# '''
# But let's finish this up and make the property read/write:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____._na.. _ n...
#
#     n... _ p....  # an "empty" prroperty - no getter or setter
#
#     0n....s...
#     ___ n... ____ value
#         ____._name _ v...
#
#     0n....ge..
#     ___ n... ____
#         r_ ____._na..
#
# # %%
# p _ ? Alex
#
# # %%
# print ?.n...
#
# # %%
# ?.n... _ 'Raymond'
#
# # %%
# print ?.n...
#
# # %%
# '''
# The deleter works the same way, and we'll come back to it soon.
# '''
#
# # %%
# '''
# Lastly you'll recall that we could set up a docstring when using the `property` callable.
# The standard technique is to simply define the docstring in the getter function:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____._na.. _ n...
#
#     0p....
#     ___ n... ____
#         """The Person's n...."""
#         r_ ____._na..
#
#     0n....s...
#     ___ n... ____ value
#         ____._na.. _ v...
#
# # %%
# # help(?.n...)
#
# # %%
# # help(?)
#
# # %%
# '''
# What happens if we set it in the setter instead?
# '''
#
# # %%
# c_ Person
#     ___ - ____ n...
#         ____._na.. _ n...
#
#     0p....
#     ___ n... ____
#         r_ ____._na..
#
#     0n....s...
#     ___ n... ____ value
#         """The Person's name."""
#         ____._na.. _ v...
#
# # %%
# # help(?.n...)
#
# # %%
# # help(?)
#
# # %%
# '''
# As you can see, the property docstring is only set on the getter. So how to set a docstring with a write-only property?
# We can do that when we create the initial property:
# '''
#
# # %%
# c_ Person
#     ___ -  ___ name
#         ____._na.. _ n...
#
#     n... _ p.... doc_'Write-only name property.'
#
#     0n....s...
#     ___ n... ____ value
#         ____._na.. _ v...
#
# # %%
# # help(?.n...)
#
# # %%
