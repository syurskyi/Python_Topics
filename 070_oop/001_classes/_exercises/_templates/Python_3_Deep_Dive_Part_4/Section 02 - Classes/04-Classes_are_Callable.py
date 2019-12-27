# # %%
# '''
# ### Classes are Callable
# '''
#
# # %%
# '''
# As we saw earlier, one of the things Python does for us when we create a class is to make it callable.
# Calling a class creates a new instance of the class - an object of that particular type.
# '''
#
# # %%
# c_ Program
#     language = 'Python'
#
#     def say_hello
#         print _*Hello from |?.l.. !*
#
# # %%
# p _ ?
#
# # %%
# print ty.. ?
#
# # %%
# print isi.. ? ?
#
# # %%
# '''
# These instances have their own namespace, and their own `__dict__` that is distinct from the class `__dict__`:
# '''
#
# # %%
# print(p.-d)
#
# # %%
# print(?.-d)
#
# # %%
# '''
# Instances also have attributes that may not be visible in their `__dict__` (they are being stored elsewhere,
#  as we'll examine later):
# '''
#
# # %%
# print(?.-c)
#
# # %%
# '''
# Although we can use `__class__` we can also use `type`:
# '''
#
# # %%
# print(ty.. ? i_ p.-c
#
# # %%
# '''
# Generally we use `type` instead of using `__class__` just like we usually use `len()` instead of accessing `__len__`.
# '''
#
# # %%
# '''
# Why? Well, one reason is that people can mess around with the `__class__` attribute:
# '''
#
# # %%
# c_ MyClass
#     p__
#
# # %%
# m = ?
#
# # %%
# print ty.. ? ?.-c
#
# # %%
# '''
# But look at what happens here:
# '''
#
# # %%
# c_ MyClass
#     -c _ st.
#
# # %%
# m _ MyClass
#
# # %%
# print ty.. ? ?.-c
#
# # %%
# '''
# So as you can see, `type` wasn't fooled!
# '''
#
# # %%
