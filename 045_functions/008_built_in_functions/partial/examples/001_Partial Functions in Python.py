from functools import *
from operator import *

# We can write partial functional application in python through functools library. Below is a simple example of partial
# function from the functools library with the add function from the operator library.

add(1, 2)
# 3
add1 = partial(add, 4)
add1(6)
# 10
add1(10)
# 14

# Partial is a higher order function which takes a function as input (like map and filter) but it also
# returns a function that can be used in the same way as any other function in your program.

list(map (add1, [1, 2, 3, 4, 5]))
# [5, 6, 7, 8, 9]
seven = partial(add1, 3)
seven()
# 7

# We can also use partial on object methods, for e.g. to generate a list of default string
#

str1 = "Hello, Python"
helloStr = partial(str1.replace, "Python")
helloStr("Tutorialspoint")
# 'Hello, Tutorialspoint'
helloStr("Java")
# 'Hello, Java'

# Partial function application is a very useful tools especially where you need to apply a range of different
# input to a single object or need to bind one of the arguments to a function to be constant.
#
# Python function helps you to write your code easily and easier to maintain.