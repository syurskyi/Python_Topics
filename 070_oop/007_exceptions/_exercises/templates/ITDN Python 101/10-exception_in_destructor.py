class MyClass(object):
    def __del__(self):
        raise ZeroDivisionError


print('Creating object')
obj = MyClass()

print('Deleting object')
del obj

print('Done')
