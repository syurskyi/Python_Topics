_______ pytest

____ Previous.friends _______ friends_teams

friends = 'Bob Dante Julian Martin'.s..


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante'), True),
    (('Bob', 'Julian'), True),
    (('Bob', 'Martin'), True),
    (('Dante', 'Julian'), True),
    (('Dante', 'Martin'), True),
    (('Julian', 'Martin'), True),
    # order does not matter
    (('Dante', 'Bob'), False),
    (('Julian', 'Bob'), False),
    (('Martin', 'Bob'), False),
    (('Julian', 'Dante'), False),
    (('Martin', 'Dante'), False),
    (('Martin', 'Julian'), False),
    # not with self
    (('Julian', 'Julian'), False),
])
___ test_team_of_two_order_does_not_matter(test_input, expected):
    """First test lists all combos"""
    combos = l..(friends_teams(friends, team_size=2, order_does_matter=False))
    ... l..(combos) __ 6
    __ expected:
        ... test_input __ combos
    ____:
        ... test_input n.. __ combos


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante'), True),
    (('Dante', 'Julian'), True),
    (('Dante', 'Martin'), True),
    # order does matter
    (('Dante', 'Bob'), True),
    (('Julian', 'Dante'), True),
    (('Martin', 'Dante'), True),
])
___ test_team_of_two_order_does_matter(test_input, expected):
    """From here on just test a subset of combos"""
    combos = l..(friends_teams(friends, team_size=2, order_does_matter=True))
    ... l..(combos) __ 12
    ... test_input __ combos


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante', 'Julian'), True),
    (('Bob', 'Dante', 'Martin'), True),
    (('Bob', 'Julian', 'Martin'), True),
    (('Dante', 'Julian', 'Martin'), True),
    # order does not matter
    (('Dante', 'Bob', 'Martin'), False),
    (('Julian', 'Martin', 'Dante'), False),
    # no one goes twice
    (('Dante', 'Dante', 'Martin'), False),
])
___ test_team_of_three_order_does_not_matter(test_input, expected):
    combos = l..(friends_teams(friends, team_size=3, order_does_matter=False))
    ... l..(combos) __ 4
    __ expected:
        ... test_input __ combos
    ____:
        ... test_input n.. __ combos


@pytest.mark.parametrize('test_input,expected', [
    (('Bob', 'Dante', 'Julian'), True),
    (('Bob', 'Dante', 'Martin'), True),
    (('Bob', 'Julian', 'Martin'), True),
    (('Dante', 'Julian', 'Martin'), True),
    # order does matter
    (('Dante', 'Bob', 'Martin'), True),
    (('Julian', 'Martin', 'Dante'), True),
])
___ test_team_of_three_order_does_matter(test_input, expected):
    combos = l..(friends_teams(friends, team_size=3, order_does_matter=True))
    ... l..(combos) __ 24
    ... test_input __ combos