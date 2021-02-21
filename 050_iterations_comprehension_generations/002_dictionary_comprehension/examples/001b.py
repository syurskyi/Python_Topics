# dict comprehension to create dict with numbers as values
print({str(i):i for i in [1,2,3,4,5]})
# {'1': 1, '3': 3, '2': 2, '5': 5, '4': 4}

# create list of fruits
fruits = ['apple', 'mango', 'banana','cherry']
# dict comprehension to create dict with fruit name as keys
print({f:len(f) for f in fruits})
# {'cherry': 6, 'mango': 5, 'apple': 5, 'banana': 6}

print({f:f.capitalize() for f in fruits})
# {'cherry': 'Cherry', 'mango': 'Mango', 'apple': 'Apple', 'banana': 'Banana'}

# dict comprehension example using enumerate function
print({f:i for i,f in enumerate(fruits)})
# {'cherry': 3, 'mango': 1, 'apple': 0, 'banana': 2}

# dict comprehension example to reverse key:value pair in a dictionary
f_dict = {f:i for i,f in enumerate(fruits)}
print(f_dict)
# {'apple': 0, 'banana': 2, 'cherry': 3, 'mango': 1}
# dict comprehension to reverse key:value pair in a dictionary
print({v:k for k,v in f_dict.items()})
# {0: 'apple', 1: 'mango', 2: 'banana', 3: 'cherry'}