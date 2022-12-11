my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print(counter, value)

# # Output:
# # 0 apple
# # 1 banana
# # 2 grapes
# # 3 pear
print()
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# # Output:
# # 1 apple
# # 2 banana
# # 3 grapes
# # 4 pear

print()
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# # Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]