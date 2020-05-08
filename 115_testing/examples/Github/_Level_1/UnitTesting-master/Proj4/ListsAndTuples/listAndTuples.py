import sys
import timeit
# https://www.youtube.com/watch?v=NI26dqhs2Rk
# Tuple is a smaller faster alternative to a list
# List contains a sequence of data surrounded by brackets
# Tuple contains a squence of data surrounded by parenthesis

""" Lists can have data added, removed, or changed
    Tuples cannot change. Tuples can be made quickly.
"""

# List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares = (1, 4, 9, 16, 25, 36)

# Display lengths
print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

# Iterate over both sequences
for p in prime_numbers:
    print("Prime: ", p)
for n in perfect_squares:
    print("Square: ", n)

print("")
print("List Methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods")
print(dir(perfect_squares))
print()

print(dir(sys))
print(help(sys.getsizeof))
print()

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))
print()

list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)
print()

## How to make tuples
empty_tuple = ()
test0 = ("a")
test1 = ("a",) # To make a tuple with just one element you need to have a comma at the end
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test0)
print(test1)
print(test2)
print(test3)
print()

# How to make tuples part 2
test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3
print(test1)
print(test2)
print(test3)
print()

# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print()

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print()

# Assigns string to variable country
country = ("Australia")
# Here country is a tuple, and it doesnt unpack contents into variable
country = ("Australia",)