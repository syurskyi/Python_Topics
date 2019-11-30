"""Пример использования json"""

import json
import os.path

data = [
    {
        'name': 'John',
        'age': 20,
    },
    {
        'name': 'Mary',
        'age': 19
    }
]

filename = os.path.join('data', 'example10.json')

# Сериализация
with open(filename, 'w') as file:
    json.dump(data, file)

# Десериализация
with open(filename, 'r') as file:
    read_data = json.load(file)
print(read_data)
