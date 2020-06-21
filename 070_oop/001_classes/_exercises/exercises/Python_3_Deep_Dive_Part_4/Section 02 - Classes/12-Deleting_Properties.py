# # %%
# '''
# ### Deleting Properties
# '''
#
# # %%
# '''
# Just like we can delete an attribute from an instance object, we can also delete a property from an instance object.
# Note that this action simply runs the deleter method, but the propertu remains defined **on the class**.
# It does not remove the property from the class, instead it is generally used to remove the property value from the
# **instance**.
# '''
#
# # %%
# '''
# Properties, like attributes, can be deleted by using the `del` keyword, or the `delattr` function.
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____.n... = n...
#
#     ___ get_name ____
#         print('getting name property value...')
#         r_ ____._na..
#
#     ___ set_name ____ value
#         print _ setting name property to |v.. ...
#         ____._name = value
#
#     ___ del_name ____
#         # delete the underlying data
#         print('deleting name property value...')
#         de. ____._na..
#
#     name _ p....fg.._g.. fs.._s... fd.._d... do._'Person name.'
#
#
# # %%
# p = ? Guido
#
# # %%
# print ?.n...
#
# # %%
# '''
# And the underlying `_name` property is in our instance dictionary:
# '''
#
# # %%
# print ?.-d
#
# # %%
# de. ?.n...
#
# # %%
# '''
# As we can see, the underlying `_name` attribute is no longer present in the instance dictionary:
# '''
#
# # %%
# print ? -d
#
# # %%
# t__
#     print ?.n...
# e____ A a_ ex
#     print ?
#
# # %%
# '''
# As you can see, the property deletion did not remove the property definition, that still exists.
# '''
#
# # %%
# '''
# Alternatively, we can use the `delattr` function as well:
# '''
#
# # %%
# p _ ? Raymond
#
# # %%
# d.... ? 'n...'
#
# # %%
# '''
# And we can of course use the decorator syntax as well:
# '''
#
# # %%
# c_ Person
#     ___ - ____ name
#         ____.n... _ n...
#
#     0p....
#     ___ n... ____
#         print('getting name property value...')
#         r_ ____._na..
#
#     0n....s..
#     ___ name ____ value
#         """Person name"""
#         print _ setting name property to |v.....
#         ____._name = value
#
#     0n....d..
#     ___ n... ____
#         # delete the underlying data
#         print('deleting name property value...')
#         del ____._na..
#
# # %%
# p = ? Alex
#
# # %%
# print ?.n...
#
# # %%
# de. ?.n...
#
# # %%
