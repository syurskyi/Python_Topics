import inspect
import linuxhint

print('Person.__doc__:')
print(linuxhint.Person.__doc__)
print()
print('getdoc(Person):')
print(inspect.getdoc(linuxhint.Person))

