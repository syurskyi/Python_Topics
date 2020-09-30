def foo(*args):
    double_list = [x * 2 for x in args]
    return double_list


print(foo(1, 3, 5))