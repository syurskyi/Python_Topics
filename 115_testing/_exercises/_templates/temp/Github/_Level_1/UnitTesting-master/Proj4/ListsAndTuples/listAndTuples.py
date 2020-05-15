______ ___
______ timeit
# https://www.youtube.com/watch?v=NI26dqhs2Rk
# Tuple is a smaller faster alternative to a list
# List contains a sequence of data surrounded by brackets
# Tuple contains a squence of data surrounded by parenthesis

""" Lists can have data added, removed, or changed
    Tuples cannot change. Tuples can be made quickly.
"""

# List example
prime_numbers _ [2, 3, 5, 7, 11, 13, 17]

# Tuple example
perfect_squares _ (1, 4, 9, 16, 25, 36)

# Display lengths
print("# Primes = ", le.(prime_numbers))
print("# Squares = ", le.(perfect_squares))

# Iterate over both sequences
___ p __ prime_numbers:
    print("Prime: ", p)
___ n __ perfect_squares:
    print("Square: ", n)

print("")
print("List Methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods")
print(dir(perfect_squares))
print()

print(dir(___))
print(help(___.getsizeof))
print()

list_eg _ [1, 2, 3, "a", "b", "c", T.., 3.14159]
tuple_eg _ (1, 2, 3, "a", "b", "c", T.., 3.14159)

print("List size = ", ___.getsizeof(list_eg))
print("Tuple size = ", ___.getsizeof(tuple_eg))
print()

list_test _ timeit.timeit(stmt_"[1, 2, 3, 4, 5]", number_1000000)
tuple_test _ timeit.timeit(stmt_"(1, 2, 3, 4, 5)", number_1000000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)
print()

## How to make tuples
empty_tuple _ ()
test0 _ ("a")
test1 _ ("a",) # To make a tuple with just one element you need to have a comma at the end
test2 _ ("a", "b")
test3 _ ("a", "b", "c")

print(empty_tuple)
print(test0)
print(test1)
print(test2)
print(test3)
print()

# How to make tuples part 2
test1 _ 1,
test2 _ 1, 2
test3 _ 1, 2, 3
print(test1)
print(test2)
print(test3)
print()

# (age, country, knows_python)
survey _ (27, "Vietnam", T..)

age _ survey[0]
country _ survey[1]
knows_python _ survey[2]

print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print()

survey2 _ (21, "Switzerland", F..)
age, country, knows_python _ survey2
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)
print()

# Assigns string to variable country
country _ ("Australia")
# Here country is a tuple, and it doesnt unpack contents into variable
country _ ("Australia",)