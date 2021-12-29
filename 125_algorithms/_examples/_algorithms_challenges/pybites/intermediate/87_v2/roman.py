def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""


    if type(decimal_number) != int or not 0 < decimal_number < 4000:
        raise ValueError("Invalid number")


    number_to_numeral = {1000: 'M',900: 'CM',500: 'D',400: 'CD',100: 'C',90:'XC',50: 'L',40: 'XL',10: 'X',9: 'IX',5: 'V',4: 'IV',1: 'I'}
    

    result = []

    for base_value,numeral in number_to_numeral.items():
        
        if base_value > decimal_number:
            continue
        value = decimal_number // base_value
        result.append(value * numeral)

        decimal_number %= base_value
        if decimal_number == 0:
            break


    return ''.join(result)
    








