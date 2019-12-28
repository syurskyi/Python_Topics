line = "The knights who say Ni!\n"
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))
print(line)
print(line.find('Ni') != -1)  # Search via method call or expression
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))  # End test via method call or slice
print(line[-len(sub):] == sub)
