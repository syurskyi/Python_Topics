"""Пример работы с функциями как с объектами первого класса"""

# Создание ссылки на объект
out = print
out('Hello')

# Сохранение ссылок на функции в структуре данных

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

operations = {
    '+': add,
    '-': sub
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))
