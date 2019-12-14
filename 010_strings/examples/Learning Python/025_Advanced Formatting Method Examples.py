import sys
print('{0:10} = {1:10}'.format('spam', 123.4567))  # In Python 3.3
print('{0:>10} = {1:<10}'.format('spam', 123.4567))
print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
print('{:10} = {:10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))
print('{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop')))
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))

print('#' * 52 + ' Hex, octal, binary')
print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))  # Hex, octal, binary

print('#' * 52 + ' Other to/from binary')
print(bin(255), int('11111111', 2), 0b11111111)  # Other to/from binary

print('#' * 52 + ' Other to/from hex')
print(hex(255), int('FF', 16), 0xFF)  # Other to/from hex

print('#' * 52 + ' Other to/from octal, in 3.X')
print(oct(255), int('377', 8), 0o377)  # Other to/from octal, in 3.X

print('#' * 52 + ' Parameters hardcoded')
print('{0:.2f}'.format(1 / 3.0))  # Parameters hardcoded

print('#' * 52 + ' Ditto for expression')
print('%.2f' % (1 / 3.0))  # Ditto for expression

print('#' * 52 + ' Take value from arguments')
print('{0:.{1}f}'.format(1 / 3.0, 4))  # Take value from arguments

print('#' * 52 + ' Ditto for expression')
print('%.*f' % (4, 1 / 3.0))  # Ditto for expression

print('#' * 52 + ' String method')
print('{0:.2f}'.format(1.2345))  # String method

print('#' * 52 + ' Built-in function')
print(format(1.2345, '.2f'))  # Built-in function

print('#' * 52 + ' Expression')
print('%.2f' % 1.2345)  # Expression
