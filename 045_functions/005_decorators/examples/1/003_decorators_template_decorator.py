# # -*- coding: utf-8 -*-

def decorator(fn):
    """Пример декоратора"""

    def decorated_fn(*args, **kwargs):
        """Модифицированная функция"""

        print('Decorated function says:')
        fn(*args, **kwargs)  # вызов изначальной функции
        print()

    return decorated_fn


@decorator
def hello():
    print('Hello!')


# Вызов декорированной функции
hello()