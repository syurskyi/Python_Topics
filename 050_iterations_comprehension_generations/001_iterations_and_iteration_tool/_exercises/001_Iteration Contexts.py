# -*- coding: utf-8 -*-

# Iteration Contexts
# Use file iterators
#
for line in open('script2.py'):
    print(line.upper(), end='')

print()
# Iteration Contexts
# Use List Comprehension

uppers =  [line.upper() for line in open('script2.py')]
print(uppers)

print()
# Iteration Contexts
# Use Map

print(map(str.upper, open('script2.py')))

print()
# Iteration Contexts
# Use List and Map

print(list(map(str.upper, open('script2.py'))))

print()
# Iteration Contexts
# Use Sorted

print(sorted(open('script2.py')))

print()
# Iteration Contexts
# Use Zip

print(list(zip(open('script2.py'),  open('script2.py'))))

print()
# Iteration Contexts
# Use Enumerate
#
print()
print(list(enumerate(open('script2.py'))))

# # Iteration Contexts
# # Use Filter
#
# print l.. ? bo.. o... script2.py
#
# print()
# # Iteration Contexts
# # Use Reduce
# ______ fun...
# ______ op...
#
# print f___.? o__.a.. o... script2.py
#
# print()
# # Iteration Contexts
# # Use Sum
#
# print ? 3, 2, 4, 1, 5, 0   # list
#
# print()
# # Iteration Contexts
# # Use Any
#
# print ? spam', '', ni
#
# print()
# # Iteration Contexts
# # Use All
#
# print ? spam '', ni
#
# print()
# # Iteration Contexts
# # Use Max
#
# print ? 3, 2, 5, 1, 4
#
# print()
# # Iteration Contexts
# # Use Min
#
# print ? 3, 2, 5, 1, 4
#
# print()
# # Iteration Contexts
# # Use Max for file
#
# print ? o.. script2.py
#
# print()
# # Iteration Contexts
# # Use Min for file
#
# print ? o.. script2.py
#
# print()
# # Iteration Contexts
# # Use List for file
# print ? o... script2.py
#
# # Iteration Contexts
# # Use Tuple for file
# print ? o... script2.py
#
# print()
# # Iteration Contexts
# # Slice assignment
# L _ 11 22 33 44   # list
# L 1;3 _ o.. script2.py
# print(L)
#
# print()
# # Iteration Contexts
# # list.extend method
# L = 11
# L.ex.. o.. script2.py
# print(L)
