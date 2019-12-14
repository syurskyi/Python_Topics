print('#' * 52 + ' Slice sections from S')
S = 'spammy'
S = S[:3] + 'xx' + S[5:]  # Slice sections from S
print(S)

print('#' * 52 + ' Replace all mm with xx in S')
S = 'spammy'
S = S.replace('mm', 'xx')  # Replace all mm with xx in S
print(S)
print('aa$bb$cc$dd'.replace('$', 'SPAM'))

S = 'xxxxSPAMxxxxSPAMxxxx'

print('#' * 52 + ' Search for position')
where = S.find('SPAM')  # Search for position

print('#' * 52 + ' Occurs at offset 4')
print(where)  # Occurs at offset 4
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)
S = 'xxxxSPAMxxxxSPAMxxxx'

print('#' * 52 + ' Replace all')
print(S.replace('SPAM', 'EGGS'))  # Replace all

print('#' * 52 + ' Replace one')
print(S.replace('SPAM', 'EGGS', 1))  # Replace one

S = 'spammy'
L = list(S)
print(L)

print('#' * 52 + ' Works for lists, not strings')
L[3] = 'x'  # Works for lists, not strings
L[4] = 'x'
print(L)
S = ''.join(L)
print(S)
print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))
