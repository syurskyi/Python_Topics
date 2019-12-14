__author__ = 'sergejyurskyj'

def function(): ...
def default(): ...
branch = {'spam': lambda: ..., # A table of callable function objects
'ham': function,
'eggs': lambda: ...}
branch.get(choice, default)()