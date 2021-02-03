def add(x, to=1):
    return x + to


def divide(x, by=2):
    return x / by


def square(x):
    return x ** 2


def invalid_op(x):
    raise Exception("Invalid operation")


def perform_operation(x, chosen_operation, operation_args=None):
    # If operation_args wasn't provided (i.e. it is None), set it to be an empty dictionary
    operation_args = operation_args or {}

    ops = {
        "add": add,
        "divide": divide,
        "square": square
    }

    chosen_operation_function = ops.get(chosen_operation, invalid_op)

    return chosen_operation_function(x, **operation_args)


def example_usage():
    x = 1
    x = perform_operation(x, "add", {"to": 4})  # Adds 4
    print(x)
    x = perform_operation(x, "add")  # Adds 1 since that's the default for 'add'
    x = perform_operation(x, "divide", {"by": 2})  # Divides by 2
    x = perform_operation(x, "square")  # Squares the number

example_usage()