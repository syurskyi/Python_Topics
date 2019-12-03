# default_except_clause
try:
    x = 3 / 0
except:
    pass

print('Program flow goes further')

# unhandled_exception
try:
    raise ValueError
except ZeroDivisionError:
    print('Division by zero')

# unhandled_exception_in_inner_try
try:
    try:
        raise ValueError('incorrect value')
    except ZeroDivisionError:
        print('division by zero')
except Exception as e:
    print(e)

# exception_in_destructor
class MyClass(object):
    def __del__(self):
        raise ZeroDivisionError


print('Creating object')
obj = MyClass()

print('Deleting object')
del obj

print('Done')

# raise_in_except
try:
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print('Exception:', error)
        raise
except ValueError:
    print('ValueError detected')

# raise_another_exception_in_except
a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError:
    raise ValueError

# raise_from
a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError as error:
    raise ValueError('variable b is incorrect') from error

# raise_from_None
a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError as error:
    raise ValueError('variable b is incorrect') from None

# else
def divide_numbers():
    while True:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            result = first_number / second_number
        except (ValueError, ZeroDivisionError) as error:
            print('Error:', error)
            print('Please try again')
            print()
        else:
            print('Result:', result)
            break


if __name__ == '__main__':
    divide_numbers()

# finally
def function_that_may_fail():
    response = None
    while response != 'y' and response != 'n':
        response = input('Raise an exception? (y/n) ')
    if response == 'y':
        raise Exception


try:
    function_that_may_fail()
except:
    print('Exception handler')
finally:
    print('Finally block')

# try-finally
try:
    2 / 0
finally:
    print('Finally block is always executed')
