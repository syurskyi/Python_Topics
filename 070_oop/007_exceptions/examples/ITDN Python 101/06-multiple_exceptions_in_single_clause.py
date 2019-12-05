def divide_numbers():
    loop = True
    while loop:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            print('Result:', first_number / second_number)
            loop = False
        except (ValueError, ZeroDivisionError) as error:
            print('Error:', error)
            print('Please try again')
            print()
            loop = True


if __name__ == '__main__':
    divide_numbers()
