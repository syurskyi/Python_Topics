# The Counter
# Counter is a subclass of dictionary object. The Counter() function in collections module takes an iterable or
# a mapping as the argument and returns a Dictionary. In this dictionary, a key is an element in the iterable or
# the mapping and value is the number of times that element exists in the iterable or the mapping.
# You have to import the Counter class before you can create a counter instance.

from collections import Counter

# Create Counter Objects
# There are multiple ways to create counter objects. The simplest way is to use Counter()
# function without any arguments.

cnt = Counter()

# You can pass an iterable (list) to Counter() function to create a counter object.

list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1]
Counter(list)

# Finally, the Counter() function can take a dictionary as an argument. In this dictionary, the value of a key should
# be the 'count' of that key.

Counter({1: 3, 2: 4})

# You can access any counter item with its key as shown below:

list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1]
cnt = Counter(list)
print(cnt[1])

# when you print cnt[1], you will get the count of 1.

# Output:
# 3

# In the above examples, cnt is an object of Counter class which is a subclass of dict. So it has all the methods of
# dict class.
# Apart from that, Counter has three additional functions:
#
#     Elements
#     Most_common([n])
#     Subtract([interable-or-mapping])
#
# The element() Function
# You can get the items of a Counter object with elements() function. It returns a list containing all the elements
# in the Counter object.
# Look at the following example:

cnt = Counter({1: 3 ,2: 4})
print(list(cnt.elements()))

# Output:
# [1, 1, 1, 2, 2, 2, 2]

# Here, we create a Counter object with a dictionary as an argument. In this Counter object, count of 1 is 3 and count
# of 2 is 4. The elements() function is called using cnt object which returns an iterator which is passed as an
# argument to the list.
# The iterator repeats 3 times over 1 returning three '1's, and repeats four times over 2 returning four '2's
# to the list. Finally, the list is printed using the print function.
# The most_common() Function
# The Counter() function returns a dictionary which is unordered. You can sort it according to the number of counts
# in each element using most_common() function of the Counter object.

list = [1, 2, 3, 4, 1, 2, 6, 7, 3, 8, 1]
cnt = Counter(list)
print(cnt.most_common())

# Output:
# [(1, 3), (2, 2), (3, 2), (4, 1), (6, 1), (7, 1), (8, 1)]

# You can see that most_common function returns a list, which is sorted based on the count of the elements.
# 1 has a count of three, therefore it is the first element of the list.
# The subtract() Function
# The subtract() takes iterable (list) or a mapping (dictionary) as an argument and deducts elements count
# using that argument. Check the following example:

cnt = Counter({1: 3, 2: 4})
deduct = {1: 1, 2: 2}
cnt.subtract(deduct)
print(cnt)

# Output:
# Counter({1: 2, 2: 2})

# You can notice that cnt object we first created, has a count of 3 for '1' and count of 4 for '2'.
# The deduct dictionary has the value '1' for key '1' and value '2' for key '2'. The subtract() function deducted 1
# count from key '1' and 2 counts from key '2'.
