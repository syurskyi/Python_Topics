# -*- coding: utf-8 -*-

"""Пример замыкания"""

def make_closure():
    variable = 42

    def closure():
        return variable

    return closure


fn = make_closure()
print(fn())
