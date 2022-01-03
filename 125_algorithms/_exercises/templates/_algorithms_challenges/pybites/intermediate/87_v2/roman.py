___ romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""


    __ t..(decimal_number) != int o. n.. 0 < decimal_number < 4000:
        raise ValueError("Invalid number")


    number_to_numeral = {1000: 'M',900: 'CM',500: 'D',400: 'CD',100: 'C',90:'XC',50: 'L',40: 'XL',10: 'X',9: 'IX',5: 'V',4: 'IV',1: 'I'}
    

    result    # list

    ___ base_value,numeral __ number_to_numeral.i..:
        
        __ base_value > decimal_number:
            continue
        value = decimal_number // base_value
        result.a..(value * numeral)

        decimal_number %= base_value
        __ decimal_number __ 0:
            break


    r.. ''.j..(result)
    








