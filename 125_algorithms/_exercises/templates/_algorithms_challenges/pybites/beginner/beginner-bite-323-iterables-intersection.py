"""
In this bite we are going to work on coding a function intersection() that searches
the common elements across its input. More specifically:

- Input to the function will be one, two or more objects which can be iterated
on (e.g., list, tuple, str)

- The function's output is a set containing the intersection across input iterables,
or an empty set if no common elements are found

Notes:

- Filter out inputs which are None or empty
- If after the filter you end up with just one iterable,
the output is a set with the unique elements in that iterable (see last example below)

Here is how it works in the Python interpreter's Read Execute Print Loop (REPL):

>>> from intersection import intersection
>>> insersection({1,2,3}, {2,3,4}, {3,4})
{3}
>>> intersection([1,2,3,"1"], {1,-1}, {})
{1}
>>> intersection(None, "this is a string")
{' ', 'a', 'g', 'h', 'i', 'n', 'r', 's', 't'}
Note: the template provides a hint to use a standard library module that can help you,
but it is not mandatory for solving this bite (i.e., there are at least two ways
to code intersection())
"""

_______ functools
____ typing _______ Iterable, Set, Any

# First attempt - crap and ugly
___ intersection(*args: Iterable) __ Set[Any]:
    # Filter out inputs, store them in a list
    # I want iterables that are not None and not empty
    # Edge condition:
    # - only empty inputs
    l    # list
    ___ input __ args:
        __ input __ n.. N.. a.. l..(input) > 0:
            l.a..(s..(input))
    # I need to handle an exception in case dealing with empty inputs
    # Then I use intersection method which takes an arbitrary number of sets
    # as input.
    # {0,1,2,3} intersection {0,1,2,3}, {3,4,5,6}, {2,3,5,6}
    ___
        first = l[0]
        r..(first.intersection(*l))
    ______ IndexError __ e:
        print(e)
        r..(s..())



print(intersection(N..))