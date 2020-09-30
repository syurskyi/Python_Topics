# Problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Score: 20


from collections ______ OrderedDict


ordered_dictionary = OrderedDict()
___ _ __ range(int(input())):
    item, price = input().rsplit(' ', 1)
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)
[print(item, ordered_dictionary[item]) ___ item __ ordered_dictionary]
