def multiply_5(x):
    return 5 * x


def cube_num(num):
    return num ** 3


my_list = [1, 2, 3, 4, 5]

mul_5_list = map(multiply_5, my_list)

# for elem in my_list:
#    print multiply_5(elem)

print mul_5_list

cube_list = map(cube_num, my_list)
print cube_list

print('#' * 52 + '  ### Using Lambda functions inside map')

mul_5_lambda_list = map(lambda x: x * 5, my_list)
print mul_5_lambda_list

cube_list_lambda = map(lambda x: x ** 3, my_list)
print cube_list_lambda

print('#' * 52 + '  ### Combining multiple iterators in one map function')

sub_5_from_cube = map(lambda x1, x2: x2 - x1, mul_5_list, cube_list)

print sub_5_from_cube

print('#' * 52 + '  # Filter')

my_list = [1, 2, 3, 4, 5, 6]

get_even = filter(lambda x: x % 2 == 0, my_list)

print get_even


def contains_hello(str_var):
    if "hello" in str_var:
        return True
    else:
        return False


my_str_list = ["hello world", "work hard", "yolo", "hello123"]

get_hello_strs = filter(contains_hello, my_str_list)

print get_hello_strs

print('#' * 52 + '  # Iter function')

my_list = [1, 2, 3, 4, 5, 6]

my_iter = iter(my_list)

print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)


# print next(my_iter)

class my_even_iter_class:
    def __init__(self, max_val):
        self.max_val = max_val

    def __iter__(self):
        self.n = 0
        return self

    # For Python 3.x
    def __next__(self):
        if self.n < self.max_val:
            self.n += 2
            return self.n
        else:
            raise StopIteration

    # For Python 2.x
    def next(self):
        return self.__next__()


my_even_obj = my_even_iter_class(6)

my_even_iter = iter(my_even_obj)

print('#' * 52 + '  ')

print next(my_even_iter)

print next(my_even_iter)

print next(my_even_iter)

# print next(my_even_iter)

