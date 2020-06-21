__author__ = 'sergejyurskyj'


print('#' * 52 + ' Tuple assignment')
a, b, c = (1, 2, 3)                               # Tuple assignment
print(a, b, c)

print('#' * 52 + ' Used in for loop')
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:          # Used in for loop
    print(a, b, c)


print('#' * 52 + ' Extended seq assignment')
a, *b, c = (1, 2, 3, 4)                           # Extended seq assignment
print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

print('#' * 52 + ' Manual slicing in 2.6')
for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:          # Manual slicing in 2.6
    a, b, c = all[0], all[1:3], all[3]
    print(a, b, c)

