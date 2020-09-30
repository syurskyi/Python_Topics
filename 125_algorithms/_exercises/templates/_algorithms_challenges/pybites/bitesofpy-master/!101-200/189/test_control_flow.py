______ pytest

from control_flow ______ filter_names


@pytest.mark.parametrize("names, expected_return", [
    (['bob'],   # list),
    (['bob', 'berta'],   # list),
    (['quit', 'ana'],   # list),
    (['12', 'bas'],   # list),
    (['ana', 'bob'], ['ana']),
    (['ana', 'bob', 'quinton'], ['ana']),
    (['bob', 'ana', 'quinton'], ['ana']),
    (['tim', 'ana', 'quinton'], ['tim', 'ana']),
    (['tim', 'quinton', 'ana'], ['tim']),
    (['tim', '1quinton', 'ana'], ['tim', 'ana']),
    (['t2im', '1quinton', 'ana'], ['ana']),
    (['t2im', '1quinton', 'a3na', '4'],   # list),
    (['tim', 'amber', 'ana', 'cindy', 'sara', 'molly', 'henry'],
     ['tim', 'amber', 'ana', 'cindy', 'sara']),
    (['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry'],
     ['tim', 'amber', 'ana', 'sara', 'molly']),
])
___ test_filter_names(names, expected_return
    assert list(filter_names(names)) __ expected_return