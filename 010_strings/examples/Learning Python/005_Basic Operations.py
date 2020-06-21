print('#' * 52 + ' Length: number of items')
print(len('abc'))  # Length: number of items

print('#' * 52 + ' Concatenation: a new string')
print('abc' + 'def')  # Concatenation: a new string

print('#' * 52 + ' Repetition: like "Ni!" + "Ni!" + ...')
print('Ni!' * 4)  # Repetition: like "Ni!" + "Ni!" + ...

print('#' * 52 + ' 80 dashes, the hard way')
print('------- ...more... ---')  # 80 dashes, the hard way

print('#' * 52 + ' 80 dashes, the easy way')
print('-' * 80)  # 80 dashes, the easy way

print('#' * 52 + ' Step through items, print each (3.X form)')
myjob = "hacker"
for c in myjob:
    print(c, end=' ')  # Step through items, print each (3.X form)
print()

print('#' * 52 + ' Found')
print("k" in myjob)  # Found

print('#' * 52 + ' Not found')
print("z" in myjob)  # Not found

print('#' * 52 + ' Substring search, no position returned')
print('spam' in 'abcspamdef')  # Substring search, no position returned
