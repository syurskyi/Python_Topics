c_ PhoneBook:

    ___  - 
        numbers _ {}

    ___ add  name, number
        numbers[name] _ number

    ___ lookup  name
        r_ numbers[name]

    ___ is_consistent
        for name1, number1 in numbers.items(
            for name2, number2 in numbers.items(
                __ name1 __ name2:
                    __ number1 __ number2:
                        continue
                __ number1.startswith(number2
                    r_ False
        r_ True
    
    ___ get_names
        r_ numbers.keys()

    ___ get_numbers
        r_ numbers.values()
