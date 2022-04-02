_______ p__

____ js _______ JsObject __ JS


?p__.f..
___ D
    """Create a JsObject object"""
    r.. JS(a=1, b=2, c=3)


___ test_object_type(D
    ... t..(D) __ JS


___ test_assert_regular_dict_behavior(D
    ... D 'a'  __ 1
    ... D 'b'  __ 2
    ... D 'c'  __ 3
    D 'd'  = 4
    ... l..(D) __ 4
    del D 'b'
    ... 'b' n.. __ D
    ... l..(D) __ 3
    ... l..(D.keys __  'a', 'c', 'd'
    ... l..(D.values __ [1, 3, 4]


___ test_assert_js_behavior(D
    ... D.a __ 1
    ... D.b __ 2
    ... D.c __ 3
    D.d = 4
    ... l..(D) __ 4
    del D.b
    D.update(d..(e=5))
    ... D.e __ 5


___ test_supports_nesting(D
    D.d = JS(e=5)
    ... D.d.e __ 5
    D.d.e = JS(f=6)
    ... D.d.e.f __ 6
