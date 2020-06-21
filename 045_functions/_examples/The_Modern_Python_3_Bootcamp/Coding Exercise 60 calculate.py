# Calculate Walkthrough
#
# This solution uses dict.get() a lot. dict.get('first')  will return the value of 'first' if it exists,
# otherwise it returns None.  However, you can specify a second argument which will replace None as the default value.
# I use that in this solution a bunch of times.
#
#     I defined a dictionary called operation_lookup  that maps a string like "add" to an actual mathematical operation
#     involving the values of 'first' and 'second'
#     I create a boolean variable called is_float, which is True if kwargs contains 'make_float', otherwise it's false
#     Then I lookup the correct value from the operation_lookup dict using the operation that was specified in kwargs
#         Basically, turning something like "subtract" into:kwargs.get('first', 0) - kwargs.get('second', 0)
#         Which in turns simplifies to a number
#     I store the result in a variable called operation_value
#     I return a string containing either the specified message or the default 'The result is' string.
#     Whether operation_value  is interpolated as a float or int is determined by the is_float  variable.
#     Note: this solution will divide by zero if a 2nd argument isn't provided for divide.
#     You may want to change the default value to 1.  We learn how to handle ZeroDivisionErrors later on in the course.
#     Thanks, Scott for pointing out the issue!


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message', 'The result is'), int(operation_value))
    return final
