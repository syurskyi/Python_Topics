c_ PhoneBook:
    # pycharm smart refactoring advised to create methods on the phonebook class
    ___  - 
        numbers _ {}

    ___ add  name, number
        numbers[name] _ number

    ___ lookup  name
        r_ numbers[name]

    ___ is_consistent
        # loop over phonebook entries in double loop to compare entries
        for name1, number1 in numbers.items(
            for name2, number2 in numbers.items(
                # if names are the same i'm comparing entry with itself
                if name1 == name2:
                    continue
                # look at 2 numbers to make sure one doesnt start with the other
                if number1.startswith(number2
                    r_ False
        r_ True
