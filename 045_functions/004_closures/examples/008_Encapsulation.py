# -*- coding: utf-8 -*-

def outer(num1):
    def inner_increment(num1):  # Hidden from outer code
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

# inner_increment(10)
outer(10)