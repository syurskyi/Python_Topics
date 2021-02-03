price_list = {
'fish': 8,
'beef': 7,
'broccoli': 3,
}

def find_price(item):
    return 'The price for {} is {}'.format(item, price_list.get(
        item, 'not available'))

print(find_price('fish'))
print(find_price('cauliflower'))


########################################################################################

def operations(operator, x, y):
    return {
        'add': lambda: x+y,
        'sub': lambda: x-y,
        'mul': lambda: x*y,
        'div': lambda: x/y,
    }.get(operator, lambda: 'Not a valid operation')()

print(operations('mul', 2, 8))
print(operations('unknown', 2, 8))

######################################################################################

def show_info_about_item(chosen_item="phone"):
  if chosen_item == "phone":
    return "Handheld communication device"
  elif chosen_item == "car":
    return "Self-propelled ground vehicle"
  elif chosen_item == "dinosaur":
    return "Extinct lizard"
  else:
    return "No info available"

def show_info_about_item(chosen_item="phone"):
    info_dict = {
        "phone": "Handheld communication device",
        "car": "Self-propelled ground vehicle",
        "dinosaur": "Extinct lizard"
    }
    return info_dict.get(chosen_item, "No info available")

#########################################################################################

def add_one(x):
    return x + 1


def divide_by_two(x):
    return x / 2


def square(x):
    return x ** 2


# The not-so-good way:
def perform_operation(x, chosen_operation="add_one"):
    if chosen_operation == "add_one":
        x = add_one(x)
    elif chosen_operation == "divide_by_two":
        x = divide_by_two(x)
    elif chosen_operation == "square":
        x = square(x)
    else:
        raise Exception("Invalid operation")

    return x


def add_one(x):
    return x + 1


def divide_by_two(x):
    return x / 2


def square(x):
    return x ** 2


def invalid_op(x):
    raise Exception("Invalid operation")


# The better way:
def perform_operation(x, chosen_operation="add_one"):
    ops = {
        "add_one": add_one,
        "divide_by_two": divide_by_two,
        "square": square
    }

    chosen_operation_function = ops.get(chosen_operation, invalid_op)

    return chosen_operation_function(x)

perform_operation(10)

######################################################################################################################
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
    x = perform_operation(x, "add")  # Adds 1 since that's the default for 'add'
    x = perform_operation(x, "divide", {"by": 2})  # Divides by 2
    x = perform_operation(x, "square")  # Squares the number

#############################################################################################################
