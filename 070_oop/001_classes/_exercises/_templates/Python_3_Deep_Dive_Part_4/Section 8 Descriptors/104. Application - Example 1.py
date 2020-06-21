# # %%
# '''
# ### Application - Example 1
# '''
#
# # %%
# '''
# Now let's look at some further examples of using descriptors that provides better better reusability than using
# `property` types (remember the repeated code issue we were trying to solve in the first place!)
# '''
#
# # %%
# '''
# We have already seen that data validation works well with descriptors.
# For example, we may want our object attributes to have valid values for some of it's attributes:
# '''
#
# # %%
# c_ Int
#     ___ __set_name__ owner_cl__s prop_name
#         ?  ?
#
#     ___ __set__ instance value
#         __ no. isi.. ? in.
#             r_ V.. _*|p_n.. must be an integer.
#         ?. -d |p_n.._ v...
#
#     ___ __get__ instance owner_cl__s
#         __ ? __ N..
#             r_ ?
#         ____
#             r_ ?. -d .ge. p_n.., N..
#
#
# # %%
# c_ Float:
#     ___ __set_name__ owner_cl__s prop_name
#         p_n.. _ p_n..
#
#     ___ -s instance value
#         __ no. isi.. v.. fl..
#             r_ V.. _*|p_n.. must be a fl...
#         ?. -d |p_n.._ v..
#
#     ___ __get__ instance, value
#         __ ? __ N..
#             r_ ?
#         ____
#             r_ ?. -d .ge. p_n.., N..
#
# # %%
# c_ List
#     ___ __set_name__ owner_cl__s prop_name
#         p_n.. _ p_n..
#
#     ___ -s instance value
#         __ no. isi.. v.. li..
#             r_ V.. _*|p_n.. must be a list.
#         ?. -d |p_n.._ value
#
#     ___ -g instance value
#         __ ? __ N..
#             r_ ?
#         ____
#             r_ ?. -d .ge. p_n.. N..
#
#
#
# # %%
# '''
# We can now use these descriptors in multiple c_ definitions, and __ many times __ we want in each c_:
# '''
#
# # %%
# c_ Person
#     age _ I..
#     height _ F..
#     tags _ L..
#     favorite_foods _ L..
#
# # %%
# p _ ?
#
# # %%
# ___
#     p.age _ 12.5
# ______ V.. __ ex
#     print ?
#
# # %%
# ___
#     p.height _ 'abc'
# ______ V.. __ ex
#     print ?
#
# # %%
# ___
#     p.tags _ 'python'
# ______ V.. __ ex
#     print ?
#
# # %%
# '''
# One thing here, __ that I got rather tired of writing the same code multiple times for the descriptor cl__ses!
# (beats having to re-write the same code over and over again that we would have had with properties, but still,
# we can do better than that!)
# '''
#
# # %%
# '''
# So let's rewrite this to be a bit more generic:
# '''
#
# # %%
# c_ ValidType
#     ___ - type_
#         _? _ ?_
#
#     ___ __set_name__ owner_cl__ds prop_name
#         p_n.. _ p_n..
#
#     ___ -s instance value
#         __ no. isi.. v.. _ty..
#             r_ V.. _*|p_n.. must be of type '
#                              _*|_t___. -n
#                             |
#         ?. -d |p_n.._ v..
#
#     ___ -g instance owner_cl__s
#         __ ? __ N..
#             r_ ?
#         ____
#             r_ ?. -d .get p_n.. N..
#
# # %%
# '''
# And now we can achieve the same functionality __ before:
# '''
#
# # %%
# c_ Person
#     age _ V.. in.
#     height _ V.. fl..
#     tags _ V.. li..
#     favorite_foods _ V.. tu..
#     name _ V.. st.
#
# # %%
# p _ ?
#
# # %%
# ___
#     p.age _ 10.5
# ______ V.. __ ex
#     print ?
#
# # %%
# ___
#     p.height _ 10
# ______ V.. __ ex
#     print ?
#
# # %%
# '''
# Now I'd like to allow setting the height to an integer value, since those are a subset of fl..s
# (in the mathematicel sense). That's e__y, all I need to do __ to use the `numbers.Real` c_:
# '''
#
# # %%
# ______ num...
#
# # %%
# isi..(10.1, numbers.Real)
#
# # %%
# isi..(10, numbers.Real)
#
# # %%
# '''
# So let's tweak our `Person` c_:
# '''
#
# # %%
# c_ Person
#     age _ V... in.
#     height _ V... num__.R..
#     tags _ V... li..
#     favorite_foods _ V... tu..
#     name _ V... st.
#
# # %%
# p _ ?
# 
# # %%
# p.height _ 10
#
# # %%
# p.height
