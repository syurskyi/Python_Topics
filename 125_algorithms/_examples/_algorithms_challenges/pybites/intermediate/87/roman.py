from collections import OrderedDict

from attr.validators import deep_iterable


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""

    numeral_lookup = OrderedDict([(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")])

    if isinstance(decimal_number, int):
        if decimal_number <= 0 or decimal_number >= 4000:
            raise ValueError
    else:
        raise ValueError

    try:
        numeral = numeral_lookup[decimal_number]
        return numeral
    except Exception:
        pass

    roman_numeral = ""
    while decimal_number != 0:

        if decimal_number > 1000:
            frequency = int(decimal_number / 1000)
            decimal_number = decimal_number % 1000
            roman_numeral += frequency * numeral_lookup[1000]
        else:
            for key in sorted(numeral_lookup.keys(), reverse=True):
                if key > 4 and decimal_number % key == 0:
                    roman_numeral += numeral_lookup[decimal_number]
                    decimal_number = 0
                    break
                else:
                    frequency = decimal_number / key
                    remainder = decimal_number % key
            
                    if remainder == decimal_number:
                        continue
                    else:
                        if frequency > 1:
                            roman_numeral += int(frequency) * numeral_lookup[key]
                        else:
                            roman_numeral += numeral_lookup[key]
                        decimal_number = remainder
                        break
                        
        if decimal_number > 0 and decimal_number <= 3:
            roman_numeral += remainder * numeral_lookup[1]
            decimal_number = 0

    return roman_numeral


if __name__ == "__main__":
    print(romanize(87))
    