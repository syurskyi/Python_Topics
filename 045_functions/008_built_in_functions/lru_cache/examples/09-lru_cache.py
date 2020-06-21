"""Пример использования функции lru_cache модуля functools"""

from functools import lru_cache

# Здесь функция вычисления чисел Фибоначчи записана рекурсивно, но по
# произоводительности и расходу памяти она будет сравнима с нерекурсивной
@lru_cache(maxsize=None)
def fibonacci(index):
    if index < 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


for i in range(1, 1000):
    print(fibonacci(i))
