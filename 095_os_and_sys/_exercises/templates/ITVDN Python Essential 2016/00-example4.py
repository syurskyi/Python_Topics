# ________ s__
# c_ MyManager o..
#     ___ __i__ ____
#         ____.resource _ 42
#
#     ___ __e__ ____
#         print('Entered context')
#         return ____.re..
#
#     ___ __e__ ____
#         print('Left context')
#         i_ exc_type
#             print Exeption occured: |.f.. e..
#
# # with MyManager() as resource:
# #     print('Some actions with resource:', resource)
# #     raise ValueError
#
# ___ my_with manager, context_body
#     resource _ m_.__e__
#     e.._ty.. e.._va.. e.._t.. _ N.. N.. N...
#     error _ N...
#     t__
#         c._b re..
#     e____ E... a_ e
#         e.._t.. e.._v.. e.._t.. _ s__.e.._i..
#         error _ e
#     f___
#         m__.__e__ e._t.. e.._v.. e.._t..
#         i_ e__
#             r___ e___
#
# ___ c._b. re..
#     print("Some action with resource")
#     # raise ValueError
#
# m.. M... c._b.
#
# """
# c_ FileIO:
#     def __enter__(self):
#         return self
#
#     def __exit__(self):
#         self.close()
# """
