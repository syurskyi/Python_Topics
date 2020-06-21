c_ PhoneBook:
    # pycharm smart refactoring advised to create methods on the phonebook class
    ___  - 
        numbers _ {}

    ___ add  name, number
        numbers[name] _ number

    ___ l..  name
        r_ numbers[name]

    ___ i_c..
        # loop over phonebook entries in double loop to compare entries
        ___ name1, number1 __ numbers.items(
            ___ name2, number2 __ numbers.items(
                # if names are the same i'm comparing entry with itself
                __ name1 __ name2:
                    c___
                # look at 2 numbers to make sure one doesnt start with the other
                __ number1.startswith(number2
                    r_ F..
        r_ T..
