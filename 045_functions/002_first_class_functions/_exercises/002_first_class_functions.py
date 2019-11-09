# functions_are_objects


def my_function():
    print("I am a function")


print("Functions are objects", isinstance(my_function, object))

print()

# ######################################################################################################################
# You can use variables to store functions


def my_function():
    print('I am a function')


test = my_function
test()

print()
# ######################################################################################################################
# You can pass functions as parameters


def call_passed_function(incoming):
    print("Calling!")
    incoming()
    print("Called!")


call_passed_function(my_function)

print()
# ######################################################################################################################
# You can check if something could be called

print(callable(len), callable(45), callable(callable))

# print()
# ######################################################################################################################
# You can return function from a function


def return_min_function():
    return min


test = return_min_function()
min_value = test(4, 5, -9, 12)
print("Min values is",  min_value)

print()

# ######################################################################################################################
# functions_as_first_class_objects

# Создание ссылки на объект
out = print
out("Hello")

# Сохранение ссылок на функции в структуре данных


def add(x, y):
    return(x + y)


def sub(x, y):
    return(x - y)


operations = {
    '+': add,
    '-': sub
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))

print()

# ######################################################################################################################
# Functions and Methods are callable

print(callable(print))
print(callable(len))
l = [1, 2, 3]
print(callable(l.append))
s = 'abc'
print(callable(s.upper))
#
# print()
# ######################################################################################################################
# Callables always return a value:

result = print("hello")
print(result)

l = [1, 2, 3]
result = l.append(4)
print(result)
print(l)

s = 'abc'
result = s.upper()
print(result)

print()
# ######################################################################################################################
# Classes are callable:

from decimal import Decimal
callable(Decimal)
result = Decimal(10.5)
print(result)

print()
# # ######################################################################################################################
# Class instances may be callable:


class MyClass:
    def __init__(self):
        print("initializing...")
        self.counter = 0

    def __call__(self, x=1):
        self.counter += x
        print(self.counter)


my_obj = MyClass()
callable(my_obj.__init__)
callable(my_obj.__call__)
my_obj()
my_obj()
my_obj(10)

print()

