______ pytest

from js ______ JsObject as JS


@pytest.fixture
___ D(
    """Create a JsObject object"""
    r_ JS(a=1, b=2, c=3)


___ test_object_type(D
    assert type(D) __ JS


___ test_assert_regular_dict_behavior(D
    assert D['a'] __ 1
    assert D['b'] __ 2
    assert D['c'] __ 3
    D['d'] = 4
    assert le.(D) __ 4
    del D['b']
    assert 'b' not in D
    assert le.(D) __ 3
    assert list(D.keys()) __ ['a', 'c', 'd']
    assert list(D.values()) __ [1, 3, 4]


___ test_assert_js_behavior(D
    assert D.a __ 1
    assert D.b __ 2
    assert D.c __ 3
    D.d = 4
    assert le.(D) __ 4
    del D.b
    D.update(dict(e=5))
    assert D.e __ 5


___ test_supports_nesting(D
    D.d = JS(e=5)
    assert D.d.e __ 5
    D.d.e = JS(f=6)
    assert D.d.e.f __ 6