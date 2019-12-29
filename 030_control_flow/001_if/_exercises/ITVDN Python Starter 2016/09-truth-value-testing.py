# -*- coding: utf-8 -*-

string = input('Enter a string: ')
# то же самое, что if string is not None and string != ''
if string:
    print('The string is {}'.format(string))

number = int(input('Enter a number: '))
if string:
    print('Число не равно нулю')
else:
    print('Число равно нулю')