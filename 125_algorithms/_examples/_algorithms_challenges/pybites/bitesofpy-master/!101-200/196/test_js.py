import pytest

from js import JsObject as JS


@pytest.fixture
def D():
    """Create a JsObject object"""
    return JS(a=1, b=2, c=3)


def test_object_type(D):
    a__ type(D) == JS


def test_assert_regular_dict_behavior(D):
    a__ D['a'] == 1
    a__ D['b'] == 2
    a__ D['c'] == 3
    D['d'] = 4
    a__ len(D) == 4
    del D['b']
    a__ 'b' not in D
    a__ len(D) == 3
    a__ list(D.keys()) == ['a', 'c', 'd']
    a__ list(D.values()) == [1, 3, 4]


def test_assert_js_behavior(D):
    a__ D.a == 1
    a__ D.b == 2
    a__ D.c == 3
    D.d = 4
    a__ len(D) == 4
    del D.b
    D.update(dict(e=5))
    a__ D.e == 5


def test_supports_nesting(D):
    D.d = JS(e=5)
    a__ D.d.e == 5
    D.d.e = JS(f=6)
    a__ D.d.e.f == 6