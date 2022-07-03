# _______ p__
#
# ____ ? _______ ? __ JS
#
#
# ?p__.f..
# ___ D
#     """Create a JsObject object"""
#     r.. JS(a=1, b=2, c=3)
#
#
# ___ test_object_type D
#     ... t.. ? __ ?
#
#
# ___ test_assert_regular_dict_behavior D
#     ... ?'a'  __ 1
#     ... ?'b'  __ 2
#     ... ?'c'  __ 3
#     D 'd'  = 4
#     ... l..(D) __ 4
#     d.. ? 'b'
#     ... 'b' n.. __ D
#     ... l.. ? __ 3
#     ... l.. ?.k.. __  'a', 'c', 'd'
#     ... l.. ?.v.. __ [1, 3, 4]
#
#
# ___ test_assert_js_behavior D
#     ... ?.a __ 1
#     ... ?.b __ 2
#     ... ?.c __ 3
#     ?.d 4
#     ... l.. ? __ 4
#     d.. ?.b
#     ?.u.. d.. e=5
#     ... ?.e __ 5
#
#
# ___ test_supports_nesting D
#     ?.d ? e=5
#     ... ?.d.e __ 5
#     ?.d.e ? f=6
#     ... ?.d.e.f __ 6
