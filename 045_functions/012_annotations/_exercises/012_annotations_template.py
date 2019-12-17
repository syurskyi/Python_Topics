# # ######################################################################################################################
# Annotations

def my_func (a: 'annotation for a',
            b: 'annotation for b') -> 'annotation for return':
    return a * b

help(my_func)

print()
# ######################################################################################################################
# The annotations can be any expression, not just strings:

x = 3
y = 5
def my_func(a: str) -> 'a repeated' + str(max(3, 5)) + 'times':
	return  a*max(x, y)

help(my_func)

print()
# ######################################################################################################################
# Just like docstrings are stored in the __doc__ property, annotations are stored in the __annotations__ property -
# a dictionary whose keys are the parameter names, and values are the annotation.

x = 3
y = 5
def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
	return a*max(x, y)

print(my_func.__annotations__)

print()
# ######################################################################################################################
# Annotations will work with default parameters too: just specify the default after the annotation

def my_func(a: str='a', b:int=1) -> str:
    return a*b

help(my_func)
my_func()
my_func('abc', 3)
print(my_func('abc', 3))

def my_func(a: int=0, *args: 'additional args'):
    print(a, args)

print(my_func.__annotations__)

help(my_func)

print()


