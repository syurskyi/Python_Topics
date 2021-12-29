_______ pytest

____ armstrong _______ is_armstrong


@pytest.mark.parametrize('number, expected', [
    (5, True),  (153, True), (370, True),
    (371, True),  (4150, False), (2020, False),
    (9474, True), (1989, False), (11, False),
])
___ test_armstrong(number, expected):
    ... is_armstrong(number) __ expected