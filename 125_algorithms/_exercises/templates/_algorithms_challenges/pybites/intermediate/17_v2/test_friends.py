_______ p__

____ friends _______ friends_teams

friends = 'Bob Dante Julian Martin'.s..


?p__.m__.p.('test_input,expected', [
    (('Bob', 'Dante'), T..),
    (('Bob', 'Julian'), T..),
    (('Bob', 'Martin'), T..),
    (('Dante', 'Julian'), T..),
    (('Dante', 'Martin'), T..),
    (('Julian', 'Martin'), T..),
    # order does not matter
    (('Dante', 'Bob'), F..),
    (('Julian', 'Bob'), F..),
    (('Martin', 'Bob'), F..),
    (('Julian', 'Dante'), F..),
    (('Martin', 'Dante'), F..),
    (('Martin', 'Julian'), F..),
    # not with self
    (('Julian', 'Julian'), F..),
])
___ test_team_of_two_order_does_not_matter(test_input, expected):
    """First test lists all combos"""
    combos = l..(friends_teams(friends, team_size=2, order_does_matter=F..))
    ... l..(combos) __ 6
    __ expected:
        ... test_input __ combos
    ____:
        ... test_input n.. __ combos


?p__.m__.p.('test_input,expected', [
    (('Bob', 'Dante'), T..),
    (('Dante', 'Julian'), T..),
    (('Dante', 'Martin'), T..),
    # order does matter
    (('Dante', 'Bob'), T..),
    (('Julian', 'Dante'), T..),
    (('Martin', 'Dante'), T..),
])
___ test_team_of_two_order_does_matter(test_input, expected):
    """From here on just test a subset of combos"""
    combos = l..(friends_teams(friends, team_size=2, order_does_matter=T..))
    ... l..(combos) __ 12
    ... test_input __ combos


?p__.m__.p.('test_input,expected', [
    (('Bob', 'Dante', 'Julian'), T..),
    (('Bob', 'Dante', 'Martin'), T..),
    (('Bob', 'Julian', 'Martin'), T..),
    (('Dante', 'Julian', 'Martin'), T..),
    # order does not matter
    (('Dante', 'Bob', 'Martin'), F..),
    (('Julian', 'Martin', 'Dante'), F..),
    # no one goes twice
    (('Dante', 'Dante', 'Martin'), F..),
])
___ test_team_of_three_order_does_not_matter(test_input, expected):
    combos = l..(friends_teams(friends, team_size=3, order_does_matter=F..))
    ... l..(combos) __ 4
    __ expected:
        ... test_input __ combos
    ____:
        ... test_input n.. __ combos


?p__.m__.p.('test_input,expected', [
    (('Bob', 'Dante', 'Julian'), T..),
    (('Bob', 'Dante', 'Martin'), T..),
    (('Bob', 'Julian', 'Martin'), T..),
    (('Dante', 'Julian', 'Martin'), T..),
    # order does matter
    (('Dante', 'Bob', 'Martin'), T..),
    (('Julian', 'Martin', 'Dante'), T..),
])
___ test_team_of_three_order_does_matter(test_input, expected):
    combos = l..(friends_teams(friends, team_size=3, order_does_matter=T..))
    ... l..(combos) __ 24
    ... test_input __ combos
