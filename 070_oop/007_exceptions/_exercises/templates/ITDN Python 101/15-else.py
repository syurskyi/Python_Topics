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