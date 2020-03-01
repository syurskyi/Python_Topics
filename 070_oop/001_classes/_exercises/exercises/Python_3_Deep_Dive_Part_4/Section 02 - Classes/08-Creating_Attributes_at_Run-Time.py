# # %%
# '''
# ### Creating Attributes at Run-Time
# '''
#
# # %%
# '''
# We already saw that we can add attributes to instances at run-time, and that it affects just that single instance:
# '''
#
# # %%
# c_ Person
#     p_
#
# # %%
# p1 _ ?
# p2 _ ?
#
# _1.n__ _ 'Alex'
#
# # %%
# print _1.-d
#
# # %%
# print _2.-d
#
# # %%
# '''
# So what happens if we add a function as an attribute to our instances directly (we can even do the same within
# an `__init__` method, works the same way)?
# '''
#
# # %%
# '''
# Remember that if we add a function to the class itself, calling the function from the instance will result in a method.
# Here, the result is different, since we are adding the function directly to the instance, not the class:
# '''
#
# # %%
# _1.s__ _ l_____ 'Hello!'
#
# # %%
# print _1.-d
#
# # %%
# _1.s__
#
# # %%
# '''
# As you can see, that attribute is a **plain** function - it is **not** being interpreted as a **method**.
# '''
#
# # %%
# _1.s__
#
# # %%
# '''
# Of course, the other instances do not know anything about that function:
# '''
#
# # %%
# print _2.-d
#
# # %%
# '''
# So, the question becomes, **can** we create a **method** on a specific instance?
# The answer (of course!) is yes, but we have to explicitly tell Python we are setting up a method bound to that
# specific instance.
# We do this by creating a `method` type object:
# '''
#
# # %%
# f___ ty.. ______ M.Ty.
#
# # %%
# c_ Person
#     ___ __i ____, name
#         ____.n.. _ n..
#
# # %%
# _1 _ ? Eric
# _2 _ ? Alex
#
# # %%
# '''
# Now let's create a `method` object, and bind it to `p1`. First we create a function that will handle the bound object
# as it's first argument, and use the instance `name` property.
# '''
#
# # %%
# ___ say_hello ____
#     r_ _ ____.n..| says hello!'
#
# # %%
# '''
# Now we can use that function just by itself, passing in any object that has a `name` attribute:
# '''
#
# # %%
# s.. _1 s... _2
#
# # %%
# '''
# Now however, we are going to create a method bound to `p1` specifically:
# '''
#
# # %%
# _1_s._h. _ M.T. s.. _1
#
# # %%
# print _1_s..
#
# # %%
# '''
# As you can see that method is bound to the instance `p1`. But how do we call it?
# If we try to use dotted notation or a `getattr`, that won't work because the `p1` object does not know anything
# about that method:
# '''
#
# # %%
# t__
#     _1._1_s..
# e_ A.... a_ ex
#     print ?
#
# # %%
# '''
# All we need to do is add that method to the instance dictionary - giving it whatever name we want:
# '''
#
# # %%
# _1.s.. _ _1_s...
#
# # %%
# print _1.-d
#
# # %%
# '''
# OK, so now out instance knows about that method that we stored under the name `say_hello`:
# '''
#
# # %%
# _1.s..
#
# # %%
# '''
# or, we can use the `getattr` function:
# '''
#
# # %%
# g... _1 say_hello
#
# # %%
# '''
# And of course, othe instances know nothing about this:
# '''
#
# # %%
# print _2.-d
#
# # %%
# '''
# So, to create a bound method after the object has initially been created, we just create a bound method and add it
# to the instance itself.
#
# We can do it this way (what we just saw):
# '''
#
# # %%
# _1 _ ? Alex
# print _1.-d
#
# # %%
# _1.s... _ M..T.. l_____ ____ _ |____.n.. says hello' _1
#
# # %%
# _1.s..
#
# # %%
# '''
# But we can also do this from any instance method too.
# '''
#
# # %%
# '''
# #### Example
# '''
#
# # %%
# '''
# Suppose we want some class to have some functionality that is called the same way but will differ from instance
# to instance. Although we could use inheritance, here I want some kind of 'plug-in' approach and we can do this without
# inheritance, mixins, or anything like that!
# '''
#
# # %%
# f___ ty.. _______ M.T.
#
# c_ Person
#     ___ -i ____ name
#         ____.n.. _ n..
#
#     ___ register_do_work ____ func
#         s.... ____ '_do_work' M.T. f. ____
#
#     ___ do_work ____
#         do_work_method _ g... ____ '_do_work' N..
#         # if attribute exists we'll get it back, otherwise it will be None
#         i_ d._
#             r_ d._
#         e____
#             r_____ A.......  You must first register a do_work method
#
# # %%
# math_teacher _ ? Eric
# english_teacher _ ? John
#
# # %%
# '''
# Right now neither the math nor the english teacher can do any woirk because we haven't "registered" a worker yet:
# '''
#
# # %%
# t__
#     m._t_.d._
# e_____ A.. a_ ex
#     print ?
#
# # %%
# '''
# Ok, so let's do that:
# '''
#
# # %%
# ___ work_math ____
#      r_ _ ____.n..| will teach differentials today.'
#
# # %%
# m.._t__.reg.. w._m.
#
# # %%
# print m.._t__.-d
#
# # %%
# m._t_.d._
#
# # %%
# '''
# And we can create a different `do_work` method for the English teacher:
# '''
#
# # %%
# ___ work_english ____
#     r_ f'{____.n..} will analyze Hamlet today.'
#
# # %%
# e._t_.reg... w._e.
#
# # %%
# e._t_.d._
#
# # %%
