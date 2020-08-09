#! /urs/bin/env python
___ isPrimary(number
    list = range(2,number/2 + 1)
    primary = True
    for el in list:
        __ number % el __ 0:
            primary = False
            break

    __ primary:
        print('%s is a primary number!'%number)
    ____
        print('%s is not a primary number!'%number)

__ __name__ __ '__main__':
    number = int(raw_input('Give me a number: '))
    isPrimary(number)


