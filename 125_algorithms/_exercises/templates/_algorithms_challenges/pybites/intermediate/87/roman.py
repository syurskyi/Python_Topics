____ collections _______ OrderedDict

____ attr.validators _______ deep_iterable


___ romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""

    numeral_lookup = OrderedDict([(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (50, "L"), (90, "XC"), (100, "C"), (400, "CD"), (500, "D"), (900, "CM"), (1000, "M")])

    __ isi..(decimal_number, i..):
        __ decimal_number <= 0 o. decimal_number >= 4000:
            r.. ValueError
    ____:
        r.. ValueError

    try:
        numeral = numeral_lookup[decimal_number]
        r.. numeral
    except Exception:
        p..

    roman_numeral = ""
    w.... decimal_number != 0:

        __ decimal_number > 1000:
            frequency = i..(decimal_number / 1000)
            decimal_number = decimal_number % 1000
            roman_numeral += frequency * numeral_lookup[1000]
        ____:
            ___ key __ s..(numeral_lookup.k.., r.._T..:
                __ key > 4 a.. decimal_number % key __ 0:
                    roman_numeral += numeral_lookup[decimal_number]
                    decimal_number = 0
                    break
                ____:
                    frequency = decimal_number / key
                    remainder = decimal_number % key
            
                    __ remainder __ decimal_number:
                        continue
                    ____:
                        __ frequency > 1:
                            roman_numeral += i..(frequency) * numeral_lookup[key]
                        ____:
                            roman_numeral += numeral_lookup[key]
                        decimal_number = remainder
                        break
                        
        __ decimal_number > 0 a.. decimal_number <= 3:
            roman_numeral += remainder * numeral_lookup[1]
            decimal_number = 0

    r.. roman_numeral


__ __name__ __ "__main__":
    print(romanize(87))
    