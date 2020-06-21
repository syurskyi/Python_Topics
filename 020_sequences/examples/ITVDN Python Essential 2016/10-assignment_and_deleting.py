"""
Для изменяемых последовательностей характерны операции присваивания и удаления
элементов по индексу или срезу. Они реализуются при помощи специальных
методов __setitem__ и __delitem__.
"""


my_list = [1, 4, 3, 5, 7]
print(my_list)

my_list[0] = 10
print(my_list)

my_list[3:] = range(10)
print(my_list)

del my_list[0]
print(my_list)

del my_list[:]
print(my_list)
