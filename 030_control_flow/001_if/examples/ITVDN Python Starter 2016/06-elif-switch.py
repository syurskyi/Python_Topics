print('''Меню:
      1. Файл
      2. Вид
      3. Выход
''')

choice = int(input('Ваш выбор: '))

if choice == 1:
    print('Вы выбрали пункт меню "Файл"')
elif choice == 2:
    print('Вы открыли меню "Вид"')
elif choice == 3:
    print('Завершение.')
else:
    print('Некорректный выбор')