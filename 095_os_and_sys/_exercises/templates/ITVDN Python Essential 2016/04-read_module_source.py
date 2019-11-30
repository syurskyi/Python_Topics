"""Пример открытия текстового файла для чтения
с указанием кодировки"""

# __file__ - это атрибут модуля, в котором хранится имя его файла
# исходного кода
with open(__file__, 'r', encoding='utf-8-sig') as file:
    for number, line in enumerate(file):
        print('{0}\t{1}'.format(number + 1, line), end='')

print()
