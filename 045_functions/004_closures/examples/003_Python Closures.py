# -*- coding: utf-8 -*-

# A function which is defined inside another function is known as nested function.
# Nested functions are able to access variables of the enclosing scope.
# In Python, these non-local variables can be accessed only within their scope and not outside their scope.


# Python program to illustrate
# nested functions
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('Hey!')


# As we can see innerFunction() can easily be accessed inside the outerFunction body but not outside of it’s body.
# Hence, here, innerFunction() is treated as nested Function which uses text as non-local variable.

# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
#
#     It is a record that stores a function together with an environment:
#     a mapping associating each free variable of the function (variables that are used locally,
#     but defined in an enclosing scope) with the value or reference to which the name was bound
#     when the closure was created.
#     A closure—unlike a plain function—allows the function to access those captured variables through the closure’s
#     copies of their values or references, even when the function is invoked outside their scope.


# Python program to illustrate
# closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction  # Note we are returning function WITHOUT parenthesis


if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()

