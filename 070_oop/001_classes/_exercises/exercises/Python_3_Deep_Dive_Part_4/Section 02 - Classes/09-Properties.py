# # %%
# '''
# ### Properties
# '''
#
# # %%
# '''
# To be clear, here we are examining **instance** properties. That is, we define the property in the class
# we are defining, but the property itself is going to be **instance** specific, i.e. different instances will support
# different values for the property. Just like instance attributes. The main difference is that we will use accessor
# method to get, set (and optionally) delete the associated instance value.
# '''
#
# # %%
# '''
# As I mentioned in the lecture, because properties use the same dotted notation (and the same `getattr`, `setattr`
# and `delattr` functions), we do not need to **start** with properties. Often a bare attribute works just fine, and if,
# later, we decide we need to manage getting/setting/deleting the attribute value, we can switch over to properties
# without breaking our class interface. This is unlike languages like Java - and hence why in those languages it is
# recommended to **always** use getter and setter functions. *Not so* in Python!
# '''
#
# # %%
# '''
# A **property** in Python is essentially a class instance - we'll come back to what that class looks like when we study
# descriptors. For now, we are going to use the `property` function in Python which is a convenience callable essentially.
# '''
#
# # %%
# '''
# Let's start with a simple example and a bare attribute:
# '''
#
# # %%
# c_ Person:
#     ___ __init__ ____ name
#         ____.n... _ n...
#
# # %%
# '''
# So this class has a single instance **attribute**, `name`.
# '''
#
# # %%
# p _ ? Alex
#
# # %%
# '''
# And we can access and modify that attribute using either dotted notation or the `getattr` and `setattr` methods:
# '''
#
# # %%
# print ?.n...
#
# # %%
# g.... ? 'n...'
#
# # %%
# '''
# p.n... = 'John'
# '''
#
# # %%
# print ?.n...
#
# # %%
# s.... ? 'n...' Eric
#
# # %%
# print p.n...
#
# # %%
# '''
# Now suppose we wan't to disallow setting an empty string or `None` for the name. Also, we'll require the name to be
# a string.
# To do that we are going to create an instance method that will handle the logic and setting of the value.
# We also create an instance method to retrieve the attribute value.
# We'll use `_name` as the instance variable to store the name.
# '''
#
# # %%
# c_ Person
#     ___ -i ____ name
#         ____.set_name n...
#
#     ___ get_name ____
#         r_ ____._name
#
#     ___ set_name ____ value
#         i_ isi... v... st. an. le. v___.st... > 0
#             # this is valid
#             ____._name _ v__.st..
#         e___
#             r.... V.... name must be a non-empty string
#
# # %%
# p _ ? Alex
#
# # %%
# t__
#     ?.set_name 100
# e____ V.... a_ ex
#     print ?
#
# # %%
# ?.s._n. Eric
#
# # %%
# ?.g._n.
#
# # %%
# '''
# Of course, our users can still manipulate the atribute directly if they want by using the "private" attribute `_name`.
# You can't stop anyone from doing this in Python - they should know better than to do that, but we're
# all good programmers, and know what and what not to do!
# '''
#
# # %%
# '''
# The way we set up our initializer, the validation will work too:
# '''
#
# # %%
# t__
#     p _ ?('')
# e____ V.... a_ ex
#     print ?
#
# # %%
# '''
# So this works, but it's a bit of pain to use the method names. So let's turn this into a property instead.
# We start with the class we just had and tweak it a bit:
# '''
#
# # %%
# c_ Person
#     ___ -i ____, name
#         ____.n... = n...  # note how we are actually setting the value for name using the property!
#
#     ___ get_name ____
#         r_ ____._na..
#
#     ___ set_name ____ value
#         i_ isi... v... st. an. le. v___.st... > 0:
#             # this is valid
#             ____._na.. _ v____.st..
#         e___
#             r____ V.... name must be a non-empty string
#
#     name _ p... fg.._g._n. fs.._s._n.
#
# # %%
# p _ ? Alex
#
# # %%
# print ?.n...
#
# # %%
# ?.n... _ 'Eric'
#
# # %%
# t__
#     p.n... _ N.
# e____ V.... a_ ex
#     print ?
#
# # %%
# '''
# So now we have the benefit of using accessor methods, without having to call the methods explicitly.
# In fact, even `getattr` and `setattr` will work the same way:
# '''
#
# # %%
# s.... ? 'n...', 'John')  # or p.n... = 'John'
#
# # %%
# g.... ? 'n...'  # or simply p.n...
#
# # %%
# '''
# Now let's examine the instance dictionary:
# '''
#
# # %%
# print ?.--d
#
# # %%
# '''
# You'll see we can find the underlying "private" attribute we are using to store the name. But the property itself
# (`name`) is not in the dictionary.
# The property was defined in the class:
# '''
#
# # %%
# print P__.--d
#
# # %%
# '''
# And you can see it's type is `property`.
# So when we type `p.name` or `p.name = value`, Python recognizes that `'name` is a `property` and therefore uses
# the accessor methods. (How it does we'll see later when we study descriptors).
# What's interesting is that even if we muck around with the instance dictionary, Python does not get confused -
# (and as usual in Python, just because you **can** do something does not mean you **should**!)
# '''
#
# # %%
# p = P.. Alex
#
# # %%
# print ?.n...
#
# # %%
# print ?.--d
#
# # %%
# ?.--d 'n...'| _ 'John'
#
# # %%
# print ?.--d
#
# # %%
# '''
# As you can see, we now have `name` in our instance dictionary.
# Let's retrieve the `name` via dotted notation:
# '''
#
# # %%
# print ?.n...
#
# # %%
# '''
# That's obviously still using the getter method.
# And setting the name:
# '''
#
# # %%
# ?.n... _ 'Raymond'
#
# # %%
# print ?.--d
#
# # %%
# '''
# As you can see, it used the setter method.
# And the same thing happens with `setattr` and `getattr`:
# '''
#
# # %%
# g.... ? 'n...'
#
# # %%
# s.... ? 'n...' 'Python'
#
# # %%
# print ?.--d)
#
# # %%
# '''
# As you can see the `setattr` method used the property setter.
# '''
#
# # %%
# '''
# For completeness, let's see how the deleter method works:
# '''
#
# # %%
# c_ Person
#     ___ - ____ n...
#         ____._na.. _ n...
#
#     ___ get_name ____
#         print('getting n...')
#         r_ ____._na..
#
#     ___ set_name ____ value
#         print('setting n...')
#         ____._na.. _ v...
#
#     ___ del_name ____
#         print('deleting n...')
#         d.. ____._na..  # or whatever "cleanup" we want to do
#
#     name = p... g.. s.. d..
#
# # %%
# p _ ? Alex
#
# # %%
# print ?.--d
#
# # %%
# print ?.n...
#
# # %%
# ?.n... _ 'Eric'
#
# # %%
# print ?.--d
#
# # %%
# de. p.n...
#
# # %%
# print ?.--d
#
# # %%
# '''
# Now, the property still exists (since it is defined in the class) - all we did was remove the underlying value
# for the property (the `_name` instance attribute):
# '''
#
# # %%
# t__
#     ?.n...
# e_____ A.... a_ ex
#     print ?
#
# # %%
# '''
# As you can see the issue is that the getter function is trying to find `_name` in the attribute, which no longer exists.
# So the getter and setter still exist (i.e. the property still exists), so we can still assign to it:
# '''
#
# # %%
# ?.n... _ 'Alex'
#
# # %%
# print ?.n...
#
# # %%
# '''
# The last param in `property` is just a docstring. So we could do this:
# '''
#
# # %%
# c_ Person
#     """This is a Person object"""
#     ___ - ____ name
#         ____._name = n...
#
#     ___ get_name ____
#         r_ ____._na..
#
#     ___ set_name ____ value
#         ____._na.. _ v..
#
#     n... _ p... g.. s.. d.._The person's name.
#
# # %%
# p _ ? Alex
#
# # %%
# he.. ?.n..
#
# # %%
# he.. P..