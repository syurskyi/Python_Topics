# Импортирование всех имён из модуля.  Не рекомендуется для использования в
# коде, однако удобно в интерактивной сессии интерпретатора
from fibonacci import *

print(list(fibonacci_numbers(30)))
print(nth_fibonacci(1000))

gen = fibonacci_sequence()
print(next(gen))
