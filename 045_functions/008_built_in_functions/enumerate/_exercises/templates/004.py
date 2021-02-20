# # Enumerate a List
#
# L = ['apples', 'bananas', 'oranges']
# ___ idx, val __ ? ?
#   print("index is $ and value is $"  ? ?
#
#
# # index is 0 and value is apples
# # index is 1 and value is bananas
# # index is 2 and value is oranges
#
#
# # Enumerate a Tuple
#
# t = ('apples', 'bananas', 'oranges')
# ___ idx, val __ ? ?
#   print("index is $ and value is $"  ? ?
#
# # index is 0 and value is apples
# # index is 1 and value is bananas
# # index is 2 and value is oranges
#
# # Enumerate a List of Tuples (The Neat Way)
#
# L = [('Matt', 20), ('Karim', 30), ('Maya', 40)]
#
# ___ idx, val __ ? ?
#   name = ? 0
#   age = ? 1
#   print("index is $, name is $, and age is $" \
#           ? ? ?
#
# # index is 0, name is Matt, and age is 20
# # index is 1, name is Karim, and age is 30
# # index is 2, name is Maya, and age is 40
#
# ___ idx |name age __ ? ?
#   print("index is $, name is $, and age is $" \
#          ? ? ?
#
# # Enumerate a String
#
# str = "Python"
# ___ idx, ch __ ? ?
#   print("index is $ and character is $" \
#           ? ?
#
#
# # index is 0 and character is P
# # index is 1 and character is y
# # index is 2 and character is t
# # index is 3 and character is h
# # index is 4 and character is o
# # index is 5 and character is n
#
# # Enumerate with a Different Starting Index
#
# L = ['apples', 'bananas', 'oranges']
# ___ idx s __ ? ? s.._1
#   print("index is $ and value is $" \
#          ? ?
#
# # index is 1 and value is apples
# # index is 2 and value is bananas
# # index is 3 and value is oranges
#
# # Why It doesn’t Make Sense to Enumerate Dictionaries and Sets
#
# d = {'a': 1, 'b': 2, 'c': 3}
# ___ k v __ ?.i..
#   # k is now the key
#   # v is the value
#   print ? ?
#
# s = {'a', 'b', 'c'}
# ___ v __ ?
#   print ?
#
# # Advanced: Enumerate Deep Dive
#
# l__ ? 'a', 'b', 'c'
# # [(0, 'a'), (1, 'b'), (2, 'c')]
#
# ___ idx val __ ? 'a' 'b'
#   print ? ?
#
# # 0 a
# # 1 b
#
# ___ i __ ? 'a' 'b'
#   print ? 0 ? 1
#
# # 0 a
# # 1 b