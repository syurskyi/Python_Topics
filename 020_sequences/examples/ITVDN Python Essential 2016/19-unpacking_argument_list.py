# Функция может иметь произвольное количество аргументов. После всех
# позиционных параметров функции или вместо них (но перед теми, которые
# предполагается использовать как именованные) в её сигнатуре можно
# указать специальный аргумент с символом * перед именем. Тогда
# оставшиеся фактические параметры сохраняются в кортеже с этим именем.


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


print(multiply(2, 3))
print(multiply(1, 9, 7, 8))


# Также существует и обратная возможность. Если при вызове функции
# перед именем итерабельного объекта поставить символ *, то его элементы
# распаковываются в позиционные аргументы.


def print_person(name, age, address):
    print(name, 'is', age, 'years old and lives at', address)


data = [
    ('John', 23, '18 Spring Lane'),
    ('Kate', 18, '20 Victory Str'),
    ('Vasiliy', 20, '323 Green Ave'),
]

for person in data:
    print_person(*person)
