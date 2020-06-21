__author__ = 'sergejyurskyj'

x = 'killer rabbit'
if x == 'roger':
    print("how's jessica?")
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away! Run away!')


choice = 'ham'
print({'spam':  1.25,         # A dictionary-based 'switch'
       'ham':   1.99,         # Use has_key or get for default
       'eggs':  0.99,
       'bacon': 1.10}[choice])



if choice == 'spam':
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')
