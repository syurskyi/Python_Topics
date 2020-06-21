S = 'abcdefghijklmnop'
print('#' * 52 + ' Skipping items')
print(S[1:10:2])  # Skipping items
print(S[::2])

S = 'hello'
print('#' * 52 + ' Reversing items')
print(S[::-1])  # Reversing items

S = 'abcedfg'
print('#' * 52 + ' Bounds roles differ')
print(S[5:1:-1])  # Bounds roles differ

print('#' * 52 + ' Slicing syntax')
print('spam'[1:3])  # Slicing syntax
print('#' * 52 + ' Slice objects with index syntax + object')
print('spam'[slice(1, 3)])  # Slice objects with index syntax + object
print('spam'[::-1])
print('spam'[slice(None, None, -1)])
