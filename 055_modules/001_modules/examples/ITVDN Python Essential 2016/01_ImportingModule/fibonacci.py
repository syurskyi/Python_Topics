"""Модуль, содержащий функции для вычисления чисел Фибоначчи"""


def fibonacci_sequence():
    """Генератор бесконечной последовательности чисел Фибоначчи"""

    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def fibonacci_numbers(count):
    """Генератор первых count чисел Фибоначчи"""

    for _, number in zip(range(count), fibonacci_sequence()):
        yield number


def nth_fibonacci(index):
    """Функция получения числа Фибоначчи по его номеру.
    Выбрасывает IndexError, если индекс меньше, чем 1.
    """

    if index < 1:
        raise IndexError('Index must be greater than or equal to 1')

    for number in fibonacci_numbers(index):
        pass

    return number