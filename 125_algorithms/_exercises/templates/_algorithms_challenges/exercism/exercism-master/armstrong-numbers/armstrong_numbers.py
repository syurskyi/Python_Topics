___ get_digits(number
    r_ list(map(int, list(str(number))))


___ is_armstrong(number
    digits = get_digits(number)
    num_digits = le.(digits)
    digits_raised_to_num_digits = [digit ** num_digits ___ digit __ digits]

    r_ number __ su.(digits_raised_to_num_digits)
