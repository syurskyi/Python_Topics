# # List comprehension
# # ==================
#
# # new_list = [new_item for item in list_or_range]
#
# numbers = [1, 2, 3, 4, 5]
# # n
# new_numbers = ? + 1 ___ ? __ ?
# print ?
#
# nato_phonetic_alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
#                           "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango",
#                           "Uniform", "Victor", "Whisky", "X-ray", "Yankee", "Zulu"]
#
# name = "John Patmore"
# # letter
# letters_list = ?.u..  ___ ? __ ?
# print ?
#
# # n
# double = ? * 2 ___ ? __ ra.. 1 5
# print ?
#
#
# # Conditional list comprehension
# # ==============================
#
# # new_list = [new_item for item in list if test]
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# # name
# short_name = ? ___ ? __ ? __ le_ ? < 5
# print ?
# caps_names =  ?.u..  ___ ? __ ? __ le_ ? > 5
# print ?
#
#
# # Tests
# # =====
#
# numbers = [1, 1]
# # i
# ___ ? __ ra.. 2 10
#     ?.ap.. ? ?-2  + ? ?-1
# print ?
#
# # n
# squared_numbers = ?**2 ___ ? __ ?  # ** = exponent operator
# print ?
#
# # n
# result = ? ___ ? __ ? __ ? % 2 __
# print ?
#
# # Create a list called result which contains the numbers
# # that are common in both files file1.txt and file2.txt.
# # The result should be a list that contains Integers, not Strings.
#
# # n
# w___ o.. *file1.txt __ file
#     file1 _  in. ?.s.. ___ ? __ ?.r_l_  # .r.. returns a list!
# print(file1)
#
# w___ o.. *file2.txt __ file
#     file2 _ in. ?.s.. ___ ? __ ?.r_l_  # .r.. returns a list!
# print ?
#
# result = ? ___ ? __ _1 __ ? __ _2
# print(result)
#
# # Dictionary Comprehension
# # ========================
#
# # new_dict = {new_key:newvalue for item in list}
# # new_dict = {new_key:newvalue for item in list if test}
# # new_dict = {new_key:newvalue for (key,value) in dict.items()}
# # new_dict = {new_key:newvalue for (key,value) in dict.items() if test}
#
# ______ ra..
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# # name
# student_scores _ ? ra__.ran__ 0 100 ___ ? __ ?
# print ?
#
# # item
# ___ ? __ ?.i..
#     print ?
# # passed_students = {item[0]: item[1] for item in student_scores.items() if item[1] >= 60}
# # student, score
# passed_students = ? ? ___ ? ? __ ?.i.. __ ? >_ 60
# print ?
#
#
# # Tests
# # =====
#
# # Create a dictionary called result that takes each word in the given sentence
# # and calculates the number of letters in each word
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Break sentence into words list
# # word
# result = ? le_ ? ___ ? __ ?.st__ "?" .sp..
# print ?
#
# # Create a dictionary called weather_f that takes each temperature in degrees Celcius
# # and converts it into degrees Fahrenheit.
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # day , C
# weather_f = ? |? * 9 / 5 + 32 ___ ? ? __ ?.i..
# print ?
#
#
# # Iterate over a Pandas DataFrame
# # ===============================
#
# # new_dict = {new_key:new_value for (index, row) in df.iterrows()}
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98],
# }
# # Looping through dictionaries:
# # key, value
# ___ ? ? __ ?.i..
#     print ? ?
#
# ______ pa...
#
# # Create Pandas DataFrame
# student_dataframe = pa__.D..F.. ?
# print?
# # Looping through DataFrame
# # key, value
# ___ ? ? __ ?.i..
#     print ?
#     print ?
#
# # Pandas in-built loop - iterrows() - Loops through rows instead of columns
# # Because iterrows returns a Series for each row, it does not preserve dtypes across the rows
# #   To preserve dtypes while iterating over the rows, it is better to use itertuples()
# #   which returns namedtuples of the values and which is generally faster than iterrows.
# # You should never modify something you are iterating over.
# #   This is not guaranteed to work in all cases.
# #   Depending on the data types, the iterator returns a copy and not a view,
# #   and writing to it will have no effect.
#
# # index, row
# ___ ? ? __ ?.i_r_
#     print("row = \n" ?  # Each row is a Pandas Series object
#     print("row.student = \n" ?.?
#     print("row.score = \n" ?.?
#
# # Create dictionary from DataFrame
# # row, index
# new_dict = ?.stu.. ?.sc.. ___ ? ? __ ?.i_r_
# print ?
# """{'Angela': 56, 'James': 76, 'Lily': 98}"""
#
# # Challenge
# # =========
#
# password_list # list
# nr_letters = ra__.ran__(8, 10)
# nr_numbers = ra__.ran__(2, 4)
# nr_symbols = ra__.ran__(2, 4)
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "_"]
#
# # char
# ___ ? __ ra.. _l..
#     ?.ap.. ra__.ch.. le..
#
# # Convert the above for loop to a list comprehension
# # new_list = [new_item for item in list if test]
#
# pwd_letters = ra__.ch.. le.. ___ _ __ ra.. _l
# pwd_numbers = ra__.ch.. nu.. ___ _ __ ra.. _n
# pwd_symbols = ra__.ch.. sy.. ___ _ __ ra.. _s
# password_list = ? + ? + ?