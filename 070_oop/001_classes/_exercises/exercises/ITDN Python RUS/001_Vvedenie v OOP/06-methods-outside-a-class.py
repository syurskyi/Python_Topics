# -*- coding: utf-8 -*-

# Атрибуты класса, которые являются функциями, -- это такие же
# атрибуты класса, как и переменные. Это можно увидеть на
# следующем примере.


def outer_method(self):
    print('I am a method of object', self)


class MyClass:
    method = outer_method


obj = MyClass()
obj.method()