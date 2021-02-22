dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Put all keys of `dict1` in a list and returns the list
print(dict1.keys())
# dict_keys(['c', 'd', 'a', 'b'])

# Put all values saved in `dict1` in a list and returns the list
print(dict1.values())

dict1.items()
# dict_items([('c', 3), ('d', 4), ('a', 1), ('b', 2)])

# dict_variable = {key:value for (key,value) in dictonary.items()}

dict1_keys = {k*2:v for (k,v) in dict1.items()}
print(dict1_keys)

# Why Use Dictionary Comprehension?
#
# Dictionary comprehension is a powerful concept and can be used to substitute for loops and lambda functions.
# However, not all for loop can be written as a dictionary comprehension but all dictionary comprehension
# can be written with a for loop.

numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)

# {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}

# Use dictionary comprehension
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

print(new_dict_comp)

# {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}

# Alternative to for loops
#
# For loops are used to repeat a certain operation or a block of instructions in a program for a given number of times.
# However, nested for loops (for loop inside another for loop) can get confusing and complex.
# Dictionary comprehensions are better in such situations and can simplify the readability and your understanding
# of the code.

# Alternative to lambda functions
#
# Lambda functions are a way of creating small anonymous functions. They are functions without a name.
# These functions are throw-away functions, which are only needed where they have been created.
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce().
#
# Let's look at the lambda function along with the map() function:

# Initialize `fahrenheit` dictionary
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)
# {'t2': -28.88888888888889, 't3': -23.333333333333336, 't1': -34.44444444444444, 't4': -17.77777777777778}

########################################################################################################################
# Initialize the `fahrenheit` dictionary
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)

# {'t2': -28.88888888888889, 't3': -23.333333333333336, 't1': -34.44444444444444, 't4': -17.77777777777778}

# Adding Conditionals to Dictionary Comprehension

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}

print(dict1_cond)
# {'e': 5, 'c': 3, 'd': 4}

# Multiple If Conditions

dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)
# {'d': 4}

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
dict1_tripleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0 if v%3 == 0}
print(dict1_tripleCond)
{'f': 6}

# In a for loop, this will correspond to:

dict1_tripleCond = {}

for (k,v) in dict1.items():
    if (v>=2 and v%2 == 0 and v%3 == 0):
            dict1_tripleCond[k] = v

print(dict1_tripleCond)
# {'f': 6}

# If-Else Conditions

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}

print(dict1_tripleCond)
# {'f': 'even', 'c': 'odd', 'b': 'even', 'd': 'even', 'e': 'odd', 'a': 'odd'}

# Nested Dictionary Comprehension
nested_dict = {'first':{'a':1}, 'second':{'b':2}}
print()
print(nested_dict.items())
print()
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)
# {'first': {1.0}, 'second': {2.0}}


nested_dict = {'first':{'a':1}, 'second':{'b':2}}

for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})
nested_dict.update({outer_k:outer_v})

print(nested_dict)
# {'first': {'a': 1.0}, 'second': {'b': 2.0}}