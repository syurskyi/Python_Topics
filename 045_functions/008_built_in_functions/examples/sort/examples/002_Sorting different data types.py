# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print sorted(x)

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print sorted(x)

# String-sorted based on ASCII translations
x = "python"
print sorted(x)

# Dictionary
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6}
print sorted(x)

# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print sorted(x)

# Frozen Set
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print sorted(x)

# Output :
# ['e', 'q', 'r', 't', 'w', 'y']
# ['e', 'q', 'r', 't', 'w', 'y']
# ['h', 'n', 'o', 'p', 't', 'y']
# ['e', 'q', 'r', 't', 'w', 'y']
# ['e', 'q', 'r', 't', 'w', 'y']
# ['e', 'q', 'r', 't', 'w', 'y']