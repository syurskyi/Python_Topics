# ______ c___
#
#
# c_ SelfReferencingEntity
#     ___ -
#         parent _ N..
#
#     ___ set_parent parent
#         ??  ?
#
#
# c_ SomeComponent
#     """
#     Python provides its own interface of Prototype via `copy.copy` and
#     `copy.deepcopy` functions. And any class that wants to implement custom
#     implementations have to override `__copy__` and `__deepcopy__` member
#     functions.
#     """
#
#     ___ - some_int some_list_of_objects some_circular_ref
#         ??  ?
#         ??  ?
#         ??  ?
#
#     ___ __copy__
#         """
#         Create a shallow copy. This method will be called whenever someone calls
#         `copy.copy` with this object and the returned value is returned as the
#         new shallow copy.
#         """
#         new _ . -c|
#             s_i.. s_l.. s_c..
#         )
#         ?. -d .u..?-d
#
#         # The new object has a new list of objects but with same
#         # objects(shared).
#         ?.s_l.. _ ______.______ s_l..
#         ?.s_c.. _ ______.______ s_c..
#         r_ ?
#
#     ___ __deepcopy__ memo_||   #dict
#         """
#         Create a deep copy. This method will be called whenever someone calls
#         `copy.deepcopy` with this object and the returned value is returned as
#         the new deep copy.
#
#         What is the use of the argument `memo`? Memo is the dictionary that is
#         used by the `deepcopy` library to prevent infinite recursive copies in
#         instances of circular references. Pass it to all the `deepcopy` calls
#         you make in the `__deepcopy__` implementation to prevent infinite
#         recursions.
#         """
#         new _ . -c |
#             s_i.. s_l.. s_c..
#         )
#         ?. -d .u.. ?-d
#
#         # The new object has a new list of objects with different copy of those
#         # objects.
#         ?.s_l.. _ ______.d.. s_l.. m..
#         ?.s_c.. _ ______.d.. s_c.. m..
#         r_ ?
#
#
# __ ______ __ ______
#
#     list_of_objects _ [1, {1, 2, 3}, [1, 2, 3]]
#     circular_ref _ SelfR..
#     component _ So.. 23, ? ?
#     c_r__.s_p.. ?
#
#     shallow_copied_component _ c___.c___ c..
#
#     # Let's change the list in shallow_copied_component and see if it changes in
#     # component.
#     sh__.s_l...ap.. ("another object")
#     __ c___.s_l.. -1 __ "another object"
#         print(
#             "Adding elements to `shallow_copied_component`'s "
#             "some_list_of_objects adds it to `component`'s "
#             "some_list_of_objects."
#         )
#     ____
#         print(
#             "Adding elements to `shallow_copied_component`'s "
#             "some_list_of_objects doesn't add it to `component`'s "
#             "some_list_of_objects."
#         )
#
#     # Let's change the set in the list of objects.
#     c___.s_l.. 1 .a.. 4
#     __ 4 __ sh__.s_l.. 1
#         print(
#             "Changing objects in the `component`'s some_list_of_objects "
#             "changes that object in `shallow_copied_component`'s "
#             "some_list_of_objects."
#         )
#     ____
#         print(
#             "Changing objects in the `component`'s some_list_of_objects "
#             "doesn't change that object in `shallow_copied_component`'s "
#             "some_list_of_objects."
#         )
#
#     deep_copied_component _ ______.de.. c___
#
#     # Let's change the list in shallow_copied_component and see if it changes in
#     # component.
#     ?.s_l...ap.. "another object"
#     __ c___.s_l.. -1 __ "another object":
#         print(
#             "Adding elements to `deep_copied_component`'s "
#             "some_list_of_objects adds it to `component`'s "
#             "some_list_of_objects."
#         )
#     ____
#         print(
#             "Adding elements to `deep_copied_component`'s "
#             "some_list_of_objects doesn't add it to `component`'s "
#             "some_list_of_objects."
#         )
#
#     # Let's change the set in the list of objects.
#     c___.s_l.. 1 .ad. 10
#     __ 10 __ ?.s_l.. 1
#         print(
#             "Changing objects in the `component`'s some_list_of_objects "
#             "changes that object in `deep_copied_component`'s "
#             "some_list_of_objects."
#         )
#     ____
#         print(
#             "Changing objects in the `component`'s some_list_of_objects "
#             "doesn't change that object in `deep_copied_component`'s "
#             "some_list_of_objects."
#         )
#
#     print(
#         f"id(deep_copied_component.some_circular_ref.parent): "
#         "{id(deep_copied_component.some_circular_ref.parent)}"
#     )
#     print(
#         f"id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent): "
#         "{id(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent)}"
#     )
#     print(
#         "^^ This shows that deepcopied objects contain same reference, they "
#         "are not cloned repeatedly."
#     )
