def f1():
    print('function')

def decorator():
    print('before')
    f1()
    print('after')

f1()
decorator()

def f1():
    print('function')

def decorator(f):
    print('before')
    f1()
    print('after')

print()
f1()
decorator(f1)


def f1():
    print('function')

def decorator(f):
    def wrapper():
        print('before')
        f1()
        print('after')
    return wrapper

print()
f1()
new = decorator(f1)
new()

print()
f1 = decorator(f1)