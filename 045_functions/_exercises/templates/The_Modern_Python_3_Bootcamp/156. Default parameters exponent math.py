def add(a, b):
    return a+b


def math(a, b, fn=add):
    return fn(a, b)


def subtract(a, b):
    return a-b


print(math(4, 5))  # results in add(4,5) which is 9

print(math(4, 5, subtract))  # results in subtract(4,5) which is -1
