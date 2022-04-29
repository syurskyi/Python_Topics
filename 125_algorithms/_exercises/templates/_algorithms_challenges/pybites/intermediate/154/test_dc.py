# ____ d.. _______ a.. r..
#
# _______ p__
#
# ____ ? _______ ?
#
#
# ?p__.f..
# ___ bites
#     b1 ? number=1, title="sum of numbers")
#     b2 ? number=2, title="a second bite", level="Intermediate")
#     b3 ? number=3, title="a hard bite", level="Advanced")
#     ? ? ? ?
#     r.. ?
#
#
# ___ test_type_annotations
#     ... ?. -a __ 'number' i.. 'title' s.. 'level' s..
#
#
# ___ test_getting_str_for_free bites
#     e.. ? number=1, title='Sum of numbers', level='Beginner')
#     ... ? 0 __ e..
#
#
# ___ test_default_level_arg_first_bite(bites
#     ... ? 0.l.. __ 'Beginner'
#
#
# ___ test_attribute_access_second_bite bites
#     ... ? 1 .n.. __ 2
#     # title should get capitalized (use the __post_init__ method)
#     ... ? 1 .t.. __ 'A second bite'
#     ... ? 1 .l.. __ 'Intermediate'
#
#
# ___ test_my_data_class_is_mutable bites
#     b3 ? -1
#     ... ?.l.. __ 'Advanced'
#     # named tuples are immutable so would not allow this:
#     b3 r..?  level='super hard'
#     ... ?.l.. __ 'super hard'
#
#
# ___ test_can_order_bites bites
#     # not out of the box, need to set something on the data class ...
#     sorted_bites s.. bites, r.._T..
#     ... ? 0 .n.. __ 3
#     ... ? 1 .n.. __ 1
#
#
# ___ test_data_class_are_not_hashable bites
#     # this would work if namedtuples, but Bites are data classes here
#     w__ p__.r.. T..
#         s.. ?
#
#
# ___ test_data_class_can_only_be_unpacked_when_casted_to_tuple bites
#     w__ p__.r.. T..
#         number, title, level ? 0
#     # but this works:
#     ? ? ? a.. ? 0
#     ... ? __ 1
#     ... ?  __ 'Beginner'