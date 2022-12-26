"""
After creating our Decorators and Context Managers learning path we realized we did not have a
beginner decorator Bite, so here it is!

Complete the sandwich decorator which takes a function and prints === Upper bread slice ===
(defined in UPPER_SLICE) and === Lower bread slice === (defined in LOWER_SLICE) before and
after calling the passed in function (func).

And voilà applying this decorator to add_ingredients you have your sandwich (see also the tests):

>>> from sandwich import sandwich
>>> @sandwich
... def add_ingredients(ingredients):
...     print(' / '.join(ingredients))
...
>>> ingredients = ['bacon', 'lettuce', 'tomato']
>>> add_ingredients(ingredients)
=== Upper bread slice ===
bacon / lettuce / tomato
=== Lower bread slice ===
This is probably the easiest way to demo a decorator.
Even so decorators can be confusing when you start using them so
here is an article we wrote some time ago: Learning Python Decorators by Example.
"""

____ f.. _______ w..

UPPER_SLICE "=== Upper bread slice ==="
LOWER_SLICE "=== Lower bread slice ==="


___ sandwich_v1(func
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    ___ wrapped $ $$
        print(UPPER_SLICE)
        result func $ $$
        print(LOWER_SLICE)
        r.. ?
    r.. wrapped

___ sandwich_v2(func
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    ___ wrapped $ $$
        print(UPPER_SLICE)
        func $ $$
        print(LOWER_SLICE)
    r.. wrapped

@sandwich_v2
___ add_ingredients(ingredients
    print(' / '.j..(ingredients
    r.. l..(ingredients)

ingredients =  'bacon', 'lettuce', 'tomato'
print(add_ingredients(ingredients