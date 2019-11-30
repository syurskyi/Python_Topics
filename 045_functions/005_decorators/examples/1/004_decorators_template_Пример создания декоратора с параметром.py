# # -*- coding: utf-8 -*-

def cast_result(type_):
    """Пример создания декоратора с параметром"""

    def cast_decorator(function):
        """Сам декоратор"""

        def decorated_function(*args, **kwargs):
            result = function(*args, **kwargs)
            return type_(result)

        return decorated_function

    return cast_decorator


@cast_result(float)
def add(x, y):
    return x + y


print(add(2, 3))

import decimal


@cast_result(repr)
@cast_result(decimal.Decimal)
def div(x, y):
    return x / y


print(div(3, 2))