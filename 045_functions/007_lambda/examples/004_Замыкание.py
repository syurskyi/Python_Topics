# -*- coding: utf-8 -*-

def outer_func(x):
     y = 4
     def inner_func(z):
         print(f"x = {x}, y = {y}, z = {z}")
         return x + y + z
     return inner_func


for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

# Точно так же лямбда также может быть замыканием. Вот тот же пример с лямбда-функцией Python:
print('#' * 52 + '  ')


def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")

