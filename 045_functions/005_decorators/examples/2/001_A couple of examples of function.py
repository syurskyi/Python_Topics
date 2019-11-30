# # -*- coding: utf-8 -*-

def hello_world():
    print('Hello world!')

print(type(hello_world))


class Hello:
    pass

print(type(Hello))

print(type(10))

# Как вы заметили, функция hello_world принадлежит типу <class 'function'>. Это означает,
# что она является объектом класса function. Кроме того, класс, который мы определили, принадлежит классу type.
# От этого всего голова может пойти кругом, но чуть поигравшись с функцией type вы со всем разберётесь.
#
# Теперь давайте посмотрим на функции в качестве объектов первого класса.

# Мы можем хранить функции в переменных:

hello = hello_world
hello()

# Определять функции внутри других функций:

def wrapper_function():
    def hello_world():
        print('Hello world!')
    hello_world()

wrapper_function()
# Hello world!

# Передавать функции в качестве аргументов и возвращать их из других функций:

def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func

higher_order(hello_world)
# Получена функция <function hello_world at 0x032C7FA8> в качестве аргумента
# Hello world!
# <function hello_world at 0x032C7FA8>