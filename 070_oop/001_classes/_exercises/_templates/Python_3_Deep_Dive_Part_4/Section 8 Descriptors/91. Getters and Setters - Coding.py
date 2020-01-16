# # %%
# '''
# ### Getters and Setters
# '''
#
# # %%
# '''
# So far we have seen how the `__get__` method is called when we assign an instance of a descriptors to a class attribute.
# But we can access that attribute either from the class itself, or the instance - as we saw in the last lecture,
# both accesses end up calling the `__get__` method.
# '''
#
# # %%
# '''
# But what changes are the arguments passed to the method. Let's explore this:
# '''
#
# # %%
# from datetime import datetime
#
# c_ TimeUTC
#     ___ -g ____ instance owner_class
#         print _*__get__ called, _____= ____|, ?_ ?|, ? _ ?|')
#         r_ d_t_ .u_n_ i_f_
#
# # %%
# c_ Logger1
#     current_time = ?
#
# c_ Logger2
#     current_time = ?
#
# # %%
# '''
# Now let's access `current_time` from the class itself:
# '''
#
# # %%
# print L_1.c..
#
# # %%
# '''
# As you can see, the `instance` was `None` - this was because we called the descriptor from the `Logger1` class,
# not an instance of it. The `owner_class` tells us this descriptor instance is defined in the `Logger1` class.
# The same holds if we use `Logger2`:
# '''
#
# # %%
# print(L_2.c..
#
# # %%
# '''
# But if we call the descriptor via an instance instead:
# '''
#
# # %%
# l1 = L_1
# print(hex(id(l1)))
#
# # %%
# print(l1.c..
#
# # %%
# '''
# As you can see, `instance` is now the `l1` instance, and the owner class is still `Logger1`.
# The sme holds for instance of `Logger2`:
# '''
#
# # %%
# l2 = L_2
# print(hex(id(l2)))
# print(l2.current_time)
#
# # %%
# '''
# This means that we can differentiate, inside our `__get__` method whether the descriptor was accessed via the class
# or via an instance.
# Typically when a descriptor is access from the class we return the descriptor instance, and when accessed from the
# instance we return the instance specific value we want:
# '''
#
# # %%
# from datetime import datetime
#
# c_ TimeUTC
#     ___ -g ____ instance, owner_class
#         __ i.. __ N..
#             # called from c_
#             r_ ____
#         ____
#             # called from instance
#             r_ d_t_ .u_n_ i_f_
#
# # %%
# c_ Logger
#     current_time = ?
#
# # %%
# print(?.c..
#
# # %%
# l = ?
#
# # %%
# print(l.c..
#
# # %%
# '''
# This is consistent with the way properties work:
# '''
#
# # %%
# c_ Logger
#     ?p..
#     ___ current_time ____
#         r_ d_t_ .u_n_ i_f_
#
# # %%
# print(L__.c..
#
# # %%
# '''
# This returned the property instance, whereas calling it from an instance:
# '''
#
# # %%
# l = L..
# print(l.c..
#
# # %%
# '''
# Now, there is one subtle point we have to understand when we create multiple instances of a class that uses a descriptor
# as a class attribute.
# '''
#
# # %%
# '''
# Since the descriptor is assigned to an **class attribute**, all instances of the class will **share** the same
# descriptor instance!
# '''
#
# # %%
# c_ TimeUTC
#     ___ -g ____ instance owner_class
#         __ i.. __ N..
#             # called from class
#             r_ ____
#         ____
#             # called from instance
#             print _ *__get__ called in ____
#             r_ d_t_ .u_n_ i_f_
#
# c_ Logger
#     current_time = ?
#
# # %%
# l1 = ?
# l2 = ?
#
# # %%
# '''
# But look at the `current_time` for each of those instances
# '''
#
# # %%
# print(l1.current_time, l2.current_time)
#
# # %%
# '''
# As you can see the **same** instance of `TimeUTC` was used.
# '''
#
# # %%
# '''
# This does not matter in this particular example, since we just return the current time, but watch what happens if
# our property relies on some kind of state in the descriptor:
# '''
#
# # %%
# c_ Countdown
#     ___ - ____ start
#         ____.? = ? + 1
#
#     ___ -g ____ instance owner
#         __ i.. __ N..
#             r_ ____
#         ____
#             ____.? -= 1
#             r_ ____.?
#
# # %%
# c_ Rocket
#     countdown = ? 10
#
# # %%
# '''
# Now let's say we want to launch two rockets:
# '''
#
# # %%
# rocket1 = ?
# rocket2 = ?
#
# # %%
# '''
# And let's start the countdown for each one:
# '''
#
# # %%
# print(rocket1.c..
#
# # %%
# print(rocket2.c..
#
# # %%
# print(rocket1.c..
#
# # %%
# '''
# As you can see, the current countdown value is shared by both `rocket1` and `rocket2` instances of `Rocket` - this is
# because the `Countdown` instance is a class attribute of `Rocket`. So we have to be careful how we deal with instance
# level state.
# '''
#
# # %%
# '''
# The `__set__` method works in a similar way to `__get__` but it is used when we assign a value to the class attribute.
# '''
#
# # %%
# c_ IntegerValue
#     ___ -s ____ instance value
#         print _*__set__ called, ? _ ?, ? ?
#
#     ___ -g ____, instance, owner_class
#         __ i.. __ N..
#             print('__get__ called from class')
#         ____
#             print _*__get__ called, ? _ ?, ? _ ?
#
# # %%
# c_ Point2D
#     x = ?
#     y = ?
#
# # %%
# print(?.x)
#
# # %%
# p = ?
#
# # %%
# print(p.x)
#
# # %%
# p.x = 100
#
# # %%
# '''
# So, where should we store the values `x` and `y`?
# Many "tutorials" I see on the web naively store the value in the descriptor itself:
# '''
#
# # %%
# c_ IntegerValue
#     ___ -s ____ instance value
#         ____._v.. = in. v..
#
#     ___ -g ____ instance, owner_class
#         __ i.. __ N..
#             r_ ____
#         ____
#             r_ ____._v..
#
# # %%
# c_ Point2D
#     x = ?
#     y = ?
#
# # %%
# '''
# At first blush, this seems to work just fine:
# '''
#
# # %%
# p1 = ?
#
# # %%
# p1.x = 1.1
# p1.y = 2.2
#
# # %%
# print(p1.x, p1.y)
#
# # %%
# '''
# But, remember the point I was making about the instance of the descriptor (`IntegeraValue` in this case) being shared
# by all instances of the class (`Point2D` in this case)?
# '''
#
# # %%
# p2 = ?
#
# # %%
# print(p2.x, p2.y)
#
# # %%
# '''
# And of course if we set the value:
# '''
#
# # %%
# p2.x = 100.9
#
# # %%
# print(p2.x, p1.x)
#
# # %%
# '''
# So, obviously using the descriptor instance dictionary for storage at the instance level is probably not going
# to work in most cases!
# '''
#
# # %%
# '''
# And this is the reason both the `__get__` and `__set__` methods need to know which instance we are dealing with.
# '''
#
# # %%
