# List comprehension
# ==================

# new_list = [new_item for item in list_or_range]

numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

nato_phonetic_alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
                          "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango",
                          "Uniform", "Victor", "Whisky", "X-ray", "Yankee", "Zulu"]

name = "John Patmore"
letters_list = [letter.upper() for letter in name]
print(letters_list)

double = [n * 2 for n in range(1, 5)]
print(double)


# Conditional list comprehension
# ==============================

# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
print(short_name)
caps_names = [name.upper() for name in names if len(name) > 5]
print(caps_names)


# Tests
# =====

numbers = [1, 1]
for i in range(2, 10):
    numbers.append(numbers[i-2] + numbers[i-1])
print(numbers)

squared_numbers = [n**2 for n in numbers]  # ** = exponent operator
print(squared_numbers)

result = [n for n in numbers if n % 2 == 0]
print(result)

# Create a list called result which contains the numbers
# that are common in both files file1.txt and file2.txt.
# The result should be a list that contains Integers, not Strings.

with open("file1.txt") as file:
    file1 = [int(n.strip()) for n in file.readlines()]  # .readlines() returns a list!
print(file1)

with open("file2.txt") as file:
    file2 = [int(n.strip()) for n in file.readlines()]  # .readlines() returns a list!
print(file2)

result = [n for n in file1 if n in file2]
print(result)

# Dictionary Comprehension
# ========================

# new_dict = {new_key:newvalue for item in list}
# new_dict = {new_key:newvalue for item in list if test}
# new_dict = {new_key:newvalue for (key,value) in dict.items()}
# new_dict = {new_key:newvalue for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name: random.randint(0,100) for name in names}
print(student_scores)

for item in student_scores.items():
    print(item)
# passed_students = {item[0]: item[1] for item in student_scores.items() if item[1] >= 60}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)


# Tests
# =====

# Create a dictionary called result that takes each word in the given sentence
# and calculates the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Break sentence into words list
result = {word: len(word) for word in sentence.strip("?").split()}
print(result)

# Create a dictionary called weather_f that takes each temperature in degrees Celcius
# and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (C * 9 / 5 + 32) for (day, C) in weather_c.items()}
print(weather_f)


# Iterate over a Pandas DataFrame
# ===============================

# new_dict = {new_key:new_value for (index, row) in df.iterrows()}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}
# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)

import pandas

# Create Pandas DataFrame
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)
# Looping through DataFrame
for (key, value) in student_dataframe.items():
    print(key)
    print(value)

# Pandas in-built loop - iterrows() - Loops through rows instead of columns
# Because iterrows returns a Series for each row, it does not preserve dtypes across the rows
#   To preserve dtypes while iterating over the rows, it is better to use itertuples()
#   which returns namedtuples of the values and which is generally faster than iterrows.
# You should never modify something you are iterating over.
#   This is not guaranteed to work in all cases.
#   Depending on the data types, the iterator returns a copy and not a view,
#   and writing to it will have no effect.

for (index, row) in student_dataframe.iterrows():
    print("row = \n", row)  # Each row is a Pandas Series object
    print("row.student = \n", row.student)
    print("row.score = \n", row.score)

# Create dictionary from DataFrame
new_dict = {row.student: row.score for (index, row) in student_dataframe.iterrows()}
print(new_dict)
"""{'Angela': 56, 'James': 76, 'Lily': 98}"""

# Challenge
# =========

password_list = []
nr_letters = random.randint(8, 10)
nr_numbers = random.randint(2, 4)
nr_symbols = random.randint(2, 4)
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "_"]

for char in range(nr_letters):
    password_list.append(random.choice(letters))

# Convert the above for loop to a list comprehension
# new_list = [new_item for item in list if test]

pwd_letters = [random.choice(letters) for _ in range(nr_letters)]
pwd_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
pwd_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
password_list = pwd_letters + pwd_numbers + pwd_symbols