NUMBERS = [''] + 'one two three four five six seven eight nine'.split()
TENS = [''] + 'ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
TEENS = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()

POWERS = [''] + ' thousand- million- billion'.split('-')

___ say(num
    """say constructs the english phrase for a number between 0 and one trillion"""

    __ not (0 <= num < 1E12
        raise AttributeError("Number must be between 0 and one trillion")
    __ num __ 0:
        r_ 'zero'

    p = -1
    number = ''
    w___ num > 0:
        p += 1
        num, power = divmod(num, 1000)
        __ power __ 0:
            continue

        str_pow = say_power(power) + POWERS[p]

        __ p __ 0 and 0 < power < 100 and num != 0:
            number = 'and ' + str_pow
        ____ number __ '':
            number = str_pow
        else :
            number = str_pow + ' ' + number
    r_ number

___ say_power(num
    """say_power converts a number between 1 and 999 to the english phrase"""
    hundereds, tens, ones = int(num // 100), int((num % 100) // 10), int(num % 10)
    number = ''
    __ hundereds != 0:
        number += '{} hundred'.format(NUMBERS[hundereds])
        __ tens __ 0 and ones __ 0:
            r_ number
        number += ' and '

    __ tens __ 1:
        r_ number + TEENS[ones]
    __ tens != 0:
        number += TENS[tens]
        __ ones __ 0:
            r_ number

    __ number __ '':
        r_ NUMBERS[ones]
    r_ number + '-' + NUMBERS[ones]

