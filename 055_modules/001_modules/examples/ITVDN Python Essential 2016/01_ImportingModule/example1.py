# Импортирование модуля
import fibonacci

# Вывод имени модуля
print(fibonacci.__name__)  # доступ к глобальной переменной другого модуля
# Вывод имени текущего модуля
print(__name__)            # доступ к глобальной переменной текущего модуля

# Использование функций модуля
print(list(fibonacci.fibonacci_numbers(10)))
print(fibonacci.nth_fibonacci(20))
