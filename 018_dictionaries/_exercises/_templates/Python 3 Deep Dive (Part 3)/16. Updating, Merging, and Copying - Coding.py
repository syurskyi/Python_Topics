# print('#' * 52 + ' Updating an existing keys value in a dictionary is straightforward: ')
#
# d _ a 1 b 2 c 3
# d 'b _ 200
# print ?
#
# print('#' * 52 + '  ')
# d1 = 'a' 1 'b' 2
# d2 =  'c' 3 'd' 4
# d1.u.. d2
# print(d1)
#
# print('#' * 52 + ' Note how the key order is maintained and based on the order in which the dictionaries were'
#                  ' create/updated. ')
#
# d1 = a 1 b 2
# d1.u..(b=20, c=30)
# print(d1)
#
# print('#' * 52 + ' Again notice how the key order reflects the order in which the parameters were'
#                  ' specified when calling the `update` method.  ')
#
# d1 =  a 1 b 2
# d1.u.. 'c', 2), ('d', 3
# print(d1)
#
# print('#' * 52 + ' Of course we can use more complex iterables. For example we could use a generator expression: ')
# d =  a 1 b 2
# d.u.. k, or. ? ___ ? __ 'python'
# print ?
#
# print('#' * 52 + '  ')
# d1 = a 1 b 2 c 3
# d2 = b 200 d 4
# d1.u..(d2)
# print(d1)
#
# print('#' * 52 + ' #### Unpacking dictionaries  ')
#
# l1 = [1, 2, 3]
# l2 = 'abc'
# l = (*l1, *l2)
# print(l)
#
# print('#' * 52 + ' We can do something similar with dictionaries: ')
#
# d1 = a 1 b 2
# d2 = c 3 d 4
# d = $$d1, $$d2
# print ?
#
# print('#' * 52 + ' Again note how order is preserved. What happens when there are conflicting keys in the unpacking? ')
# d1 = a 1 b 2
# d2 = b 200 c 3
# d = $$d1 $$d2
# print(d)
#
# print('#' * 52 + '  ')
# conf_defaults = di__.f_k_ 'host', 'port', 'user', 'pwd', 'database'), N...
# print ?
#
# print('#' * 52 + '  ')
#
# conf_global _
#      port 5432
#      database  deepdive
#
# conf_dev _
#      host localhost
#      user  test
#      pwd   test
#
#
# conf_prod _
#      host   prodpg.deepdive.com
#      user   $prod_user
#      pwd    $prod_pwd
#      database  deepdive_prod
#
#
# config_dev _  $$c_d. $$c_g. $$c_d.
# print ?
# config_prod _  $$c_d. $$c_g. $$c_p.
# print ?
#
# print('#' * 52 + ' Another way dictionary unpacking can be really useful,'
#                  ' is for passing keyword arguments to a function:  ')
#
# ___ my_func * kw1 kw2 kw3
#     print(kw1, kw2, kw3)
#
# d = kw2 20 kw3 30 kw1 10
#
# print('#' * 52 + ' In this case, we dont really care about the order of the elements, since we will be'
#                  ' unpacking keyword arguments: ')
#
# print m.. $$?
#
# print('#' * 52 + ' Of course we can even use it this way, but here the dictionary order does matter,'
#                  ' as it will be reflected in the order in which those arguments are passed to the function: ')
#
# ___ my_func $$
#     ___ k, v __ k__.it..
#         print ? ?
#
# print m.. $$?
#
# print('#' * 52 + ' #### Copying Dictionaries  ')
# d _ a 1, 2| b 3, 4|
# d1 = ?.c..
# print(d)
# print(d1)
#
# print(id(d), id(d1), d is d1)
#
# print('#' * 52 + '  ')
# del d['a']
# print(d)
# print(d1)
# d['b'] = 100
# print(d)
# print(d1)
#
# print('#' * 52 + ' But lets see what happens if we mutate the value of one dictionary:  ')
#
# d =  a 1, 2| b  3, 4|
# d1 = ?.c..
# print(d)
# print(d1)
#
# ? 'a'.ap.. 100
# print(d)
# print(d1)
# print(d['a'] is d1['a'])
#
# print('#' * 52 + ' So if we have nested dictionaries for example, as is often the case with JSON documents,'
#                  ' we have to be careful when creating shallow copies. ')
#
# d =  id 123445
#      person |
#          name John
#          age  78
#       posts 100, 105, 200|
#
#
# d1 = ?.c..
# _1 person name _ 'John Cleese'
# _1 posts .ap.. 300
# print(d1)
# print(d)
#
# print('#' * 52 + ' If we want to avoid this issue, we have to create a **deep** copy. '
#                  ' We can easily do this ourselves using recursion, but the `copy` module implements such'
#                  ' a function for us: ')
#
# f___ co.. ______ dee..
# d =  id 123445
#      person  |
#          name  John
#          age  78
#       posts   100, 105, 200|
#
#
# d1 = dee.. ?
# _1 person name _ 'John Cleese'
# _1 posts .ap.. 300
# print(d1)
# print(d)
#
# print('#' * 52 + ' We saw earlier that we can also copy a dictionary by essentially unpacking the keys of one,'
#                  ' or more dictionaries, into another.This also creates a **shallow** copy: ')
#
# d1 =  a 1, 2| , b |3, 4
# d = $$_1
# print(d)
# _1 a' .ap.. 100
# print(d1)
# print(d)
#
# print('#' * 52 + '  ')
# f___ ra.. ______ r_i_
#
# big_d = k r_i_ 1, 100| ___ ? __ ra.. 1_000_000
#
#
# ___ copy_unpacking d
#     d1 = $$?
#
#
# ___ copy_copy d
#     d1 = ?.c..
#
#
# ___ copy_create d
#     d1 = di.. d
#
#
# ___ copy_comprehension d
#     d1 = k v ___ ? ? __ ?.it..
#
# print('#' * 52 + '  ')
# f____ ti.. ______ ti..
#
# print ti__ 'copy_unpacking(big_d)' g... _ g.. nu.. _ 100
# print ti__ 'copy_copy(big_d)', g.._g.. nu.._100
# print ti__ 'copy_create(big_d)', g.._g.. nu.._100
# print ti__ 'copy_comprehension(big_d)', g.._g.. nu.._100