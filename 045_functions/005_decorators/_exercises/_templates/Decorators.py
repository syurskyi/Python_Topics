print('#' * 52 + '  # Decorators')


def my_function():
    print "I am a simple function"


my_function()
print('#' * 52 + '  ')


def my_decorator(my_func):
    def wrapper_func():
        print "Inside Decorator"
        my_func()
        print "Decorator Finished"

    return wrapper_func


my_decorated_function = my_decorator(my_function)

my_decorated_function()

print('#' * 52 + '  # Using @ notation for decorator')

@my_decorator
def my_other_simple_function():
    print "I am another simple function"

my_other_simple_function()

print('#' * 52 + '  # Nested Decorator')


def run_multiple(num_times):
    def nested_decorator(my_func):
        def wrapper_run_multiple():
            print "Inside Inner decorator"
            for i in range(0, num_times):
                my_func()
            print "Inner decorator finished"
            # wrapper finsihed

        # Nested decorator finished
        return wrapper_run_multiple

    return nested_decorator

@run_multiple(num_times=6)
def just_another_simple_func():
    print "I am just another simple function"

print('#' * 52 + '  ')

just_another_simple_func()

print('#' * 52 + '  # Using Arguments with Decorators')

@run_multiple(num_times=8)
def func_with_args(sen1, sen2):
    print sen1 + sen2

# func_with_args("hello", "world") # TypeError: wrapper_run_multiple() takes no arguments (2 given)


def decorator_with_args(my_func):
    def wrapper_with_args(*args, **kwargs):
        print "Inside decorator"
        my_func(*args, **kwargs)
        print "Decoration done"
    return wrapper_with_args

@decorator_with_args
def func_with_args(sen1, sen2):
    print sen1 + sen2

func_with_args("hello", "world")

print('#' * 52 + '  # Nested decorators with arguments')


def run_multiple_nested(num_times):
    def decorator_with_args(my_func):
        def wrapper_with_args(*args, **kwargs):
            print "Inside decorator"
            for i in range(0, num_times):
                my_func(*args, **kwargs)
            print "Decoration done"

        return wrapper_with_args

    return decorator_with_args

@run_multiple_nested(num_times=5)
def func_with_args(sen1, sen2):
    print sen1 + sen2

func_with_args("hello", "world")

print('#' * 52 + '  ')

@run_multiple_nested(num_times=5)
def func_with_no_args():
    print "I am a function with no arguments"

func_with_no_args()