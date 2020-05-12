c_ PhoneBook:

    ___  - 
        numbers _ {}

    ___ add  name, number
        numbers[name] _ number

    ___ l..  name
        r_ numbers[name]

    ___ i_c..
        ___ name1, number1 __ numbers.items(
            ___ name2, number2 __ numbers.items(
                __ name1 __ name2:
                    __ number1 __ number2:
                        c___
                __ number1.startswith(number2
                    r_ F..
        r_ T..
    
    ___ get_names
        r_ numbers.keys()

    ___ get_numbers
        r_ numbers.values()
