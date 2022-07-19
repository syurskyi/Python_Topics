# Displaying the Keys in sorted order

# Function calling
def dictionairy():
    # Declare hash function
    key_value = {}

    # Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:-\n")

    print("key_value", key_value)

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")


dictionairy()


from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)

# Sorting the Keys and Values in Alphabetical Order using the Key

# function calling
def dictionairy():
    # Declaring the hash function
    key_value = {}

    # Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("key_value", key_value)

    print("Task 2:-\nKeys and Values sorted in",
          "alphabetical order by the key  ")

    # sorted(key_value) returns an iterator over the
    # Dictionary’s value sorted in keys.
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")


dictionairy()


# Example 4: Sorting the Keys and Values in alphabetical using the

# Function calling
def dictionairy():
    # Declaring hash function
    key_value = {}

    # Initializing the value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("key_value", key_value)

    print("Task 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv:
    (kv[1], kv[0])))



dictionairy()

# Sort Dictionary By Value in Python

# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)

sorted_value_index = np.argsort(dict.values())
dictionary_keys = list(dict.keys())
sorted_dict = {dictionary_keys[i]: sorted(
    dict.values())[i] for i in range(len(dictionary_keys))}

print(sorted_dict)
