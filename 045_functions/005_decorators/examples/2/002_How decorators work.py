# # -*- coding: utf-8 -*-

# Декоратор — это функция, которая позволяет обернуть другую функцию для расширения её
# функциональности без непосредственного изменения её кода.

def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

# Здесь decorator_function() является функцией-декоратором. Как вы могли заметить,
# она является функцией высшего порядка, так как принимает функцию в качестве аргумента, а также возвращает функцию.
# Внутри decorator_function() мы определили другую функцию, обёртку, так сказать, которая обёртывает функцию-аргумент
# и затем изменяет её поведение. Декоратор возвращает эту обёртку.

@decorator_function
def hello_world():
    print('Hello world!')

hello_world()

#  Просто добавив @decorator_function перед определением функции hello_world(), мы модифицировали её поведение.
#  Однако как вы уже могли догадаться, выражение с @ является всего лишь синтаксическим сахаром
#  для hello_world = decorator_function(hello_world).
#
# Иными словами, выражение @decorator_function вызывает decorator_function() с hello_world в качестве аргумента
# и присваивает имени hello_world возвращаемую функцию.

def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


fetch_webpage()