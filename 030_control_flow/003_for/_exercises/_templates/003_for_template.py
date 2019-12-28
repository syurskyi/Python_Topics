#!/usr/bin/python
# -*- coding: utf-8 -*-

# ######################################################################################################################
# for
# General Format
# "spam", "eggs", "ham"
# print(_, __)

# sum _ 0
# [1, 2, 3, 4]
# sum
# print(sum)

# prod _ 1
# item 1, 2, 3, 4]
# prod
# print(prod)

# print()
# ######################################################################################################################
# for
# Other data types
# S _ "lumberjack"
# T _ "and", "I'm", "okay"  # tuple
# # #  Iterate over a string
# x
# print(_, _)
# # # Iterate over a tuple
# x
# print(_, _)

# # # Iterate over a os
import os

# print(dir(os))

# os_dir =
# print(os_dir)
# x
# print(x)

# print()
# ######################################################################################################################
# for
# Tuple assignment
# T _ (1, 2), (3, 4), (5, 6)   # list
# a, b
# print(a, b)

# print()
# ######################################################################################################################
# for
# Use dict keys iterator and index
# D _ 'a' 1 'b' 2 'c' 3    # dictionary
# key in D:
# print(_ '=>' _)

# print(l_(D._()))

# print()
# ######################################################################################################################
# for
# Iterate over both keys and values
# D _ 'a' 1 'b' 2 'c' 3   # dictionary
# key value
# print(_ '=>' _)

# print()
# ######################################################################################################################
# for
# Manual assignment equivalent
# Need to check something wrong is here
# T _ (1 2) (3 4) (5 6)   # list
# both

# print(a, b)

# print()
# ######################################################################################################################
# автоматического распаковывания вложенных структур в цикле for
# ((a, b), c) _ ((1, 2), 3)
# [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)
# [([1, 2], 3), ['XY', 6]]: print(a, b, c)

#  extended sequence assignment in for loops
# Tuple assignment
# extended sequence assignment in for loops
#  Used in for loop
# a, b, c _ (1, 2, 3)
# [(1, 2, 3), (4, 5, 6)]
# print(a, b, c)

# print()
# ######################################################################################################################
#  extended sequence assignment in for loops
#  Extended seq assignment
# a, *b, c _ (1, 2, 3, 4)
# print(a, b, c)
# for loop
# a *b c [(1, 2, 3, 4), (5, 6, 7, 8)
# print(a, b, c)

# print()
# ######################################################################################################################
# Nested for loops
# Имея список объектов (items) и список ключей (tests),
# этот фрагмент пытается отыскать каждый ключ в списке объектов и сообщает о результатах поиска
# 2 options

# items _ ["aaa", 111, (4, 5), 2.01]  # A set of objects
# tests _ [(4, 5), 3.14]  # Keys to search for

# key     # For all keys
# item    # For all items
# Check for match
# print(_ "was found")


# print(_"not found!")

# key     # For all keys
# key     # Let Python check for a match
# print(_ "was found")

# print(_, "not found!")

# print()
# ######################################################################################################################
# цикла for решает типичную задачу обработки данных – выборку одинаковых элементов из двух последовательностей
# seq1 _ "spam"
# seq2 _ "scam"
# res _ []  # Start empty
# x       # Scan first sequence
# x       # Common item?
# Add to result end
# print(_)

# for
# Enumeration of letters in a word
# "str":
# print(_, _)

# print("\nЦикл выполнен")

# print()
# ######################################################################################################################
# for
# Enumeration of dictionary elements.
# arr _ "x" 1 "y" 2 "z" 3   # dictionary
# print(_._()) # Использование метода keys()

# key :  # Использование метода keys()
# print(_, _)

# key :  # Словари также поддерживают итерации
# print(_, _)
#
# arr _ "x" 1 "y" 2 "z" 3   # dictionary
# key    #  сортировать
# print(_, _)

# print()
# ######################################################################################################################
# for
# Enumeration of elements of the list of tuples
# arr _ (1 2) (3 4)  # Список кортежей
# a, b
# print(_, _)
# print()

# print()
# ######################################################################################################################
# number of vowels
# sentence _ "now is the time for all good people to come to the aid"
# count _ 0
# letter
# 'a' 'e' 'i' 'u' 'o':

# print("The number of vowels is ")

# print()
# ######################################################################################################################
# Repeating something 10 times
# elements _ [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index
# print()

# print()
# ######################################################################################################################
# for
# Using each value while you iterate

# students _ [
#     {"name": "Rolf", "grade": 90},
#     {"name": "Bob", "grade": 78},
#     {"name": "Jen", "grade": 100},
#     {"name": "Anne", "grade": 80},
# ]
# student  # student is a variable used for iteration
# name
# grade
# print(" _ has a grade of _.")

# print()
# ######################################################################################################################
# Destructuring in a loop
# friends _ [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
# name age
# print('_ is _ years old')

# print()
# ######################################################################################################################
# for
# i принимает значения в диапазоне [0, 10)
# i range(10)
# print('i =' _)
# print()
# i принимает значения в диапазоне [5, 10)
# i range(5 10)
# print('i =' _)
# print()
# i принимает значения в диапазоне [5, 10) с шагом 2
# i range(5 10 2)
# print('i =' _)


# print()
# ######################################################################################################################
# for-else, using range
# i, 3  # # цикл будет повторен три раза, если пользователь не завершит его ранее
# responce, 'Enter stop to stop the loop (else whatever): ')



# print('The cycle ended itself')  # эта ветка будет выполенена только если цикл не был прерван
# print('End of program')
# print()

# print()
# ######################################################################################################################
# for-continue
# i range(1 11)
# # #  пропускаем число 5

# print('The current number is')

# print()
# ######################################################################################################################
# nested-loops
# i range(10)
# j range(30)
# print('*')
# print()

# print()
# ######################################################################################################################
# The range () and enumerate () functions
# arr _ 1 2 3  # list

# print()
# ######################################################################################################################
# Example of using the range () function
# arr _ 1 2 3  # list

# (1 101): print(i, ...)

# (100 0 -1): print(i, ...)

# (2, 101, 2): print(i, ...)

# print()
# ######################################################################################################################
#  An example of using the enumerate () function
# arr _ 1 2 3 4 5 6  # list
# elem
# print(arr)

# print()
# ######################################################################################################################
# Enumerate a List
# You can iterate over the index and value of an item in a list by using a basic for loop
# L _ 'apples' 'bananas' 'oranges'  # list
# idx val
# print("index is ... and value is ... ")

# print()
# ######################################################################################################################
# Enumerate a Tuple
# Enumerating a tuple isn’t at all different from enumerating a list.
# t _ 'apples' 'bananas' 'oranges'   # tuple
# idx, val
# print("index is ... and value is ...")

# print()
# ######################################################################################################################
# ######################################################################################################################
# Enumerate a List of Tuples (The Neat Way)
# Say you have a list of tuples where each tuple is a name-age pair.
# With tuple unpacking, we can do something like this
# L _ [('Matt', 20), ('Karim', 30), ('Maya', 40)]
# idx val
# name
# age
# print "index is __, name is __, and age is __"

# print()
# ######################################################################################################################
# Enumerate a String
# str _ "Python"
# idx, ch
# print("index is _ and character is _")

# print()
# ######################################################################################################################
# Enumerate with a Different Starting Index
# L _ ['apples', 'bananas', 'oranges']
# idx, s
# print "index is _ and value is _"
