__author__ = 'sergejyurskyj'

S = "lumberjack"
T = ("and", "I'm", "okay")

print('#' * 52 + ' Iterate over a string')
for x in S:
    print(x)    # Iterate over a string
print()

print('#' * 52 + ' Iterate over a tuple')
for x in T:
    print(x)     # Iterate over a tuple

import os

print(dir(os))

os_dir = dir(os)
print(os_dir)

for x in os_dir:
    print(x)
