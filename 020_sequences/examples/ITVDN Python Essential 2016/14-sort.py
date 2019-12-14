"""
Метод sort() сортирует список, модифицируя его. Также существует встроенная
функция sorted, которая сортирует любой итерабельный объект, не модифицируя
его, и возвращает список.
"""

my_list = [4, 3, 2, 0, 17, -5, 3]
list_copy = my_list[:]
print(my_list)

my_list.sort()
print(my_list)

list_copy.sort(reverse=True)
print(list_copy)

print()

string = 'Lorem ipsum dolor sit amet.'
print(string)
sorted_string = sorted(string)
print(sorted_string)
print(''.join(sorted_string))
