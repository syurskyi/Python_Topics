import inspect
import sample

print('X.__doc__:')
print(sample.X.__doc__)
print()
print('getdoc(X):')
print(inspect.getdoc(sample.X))