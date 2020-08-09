#! /urs/bin/env python

__ __name__ __ '__main__':
    number = int(raw_input('Give me a number: '))
    list = range(1,number/2 + 1)
    divisors = []
    for el in list:
        __ number % el __ 0:
            divisors.append(el)

    print('The divisors of ' + str(number) + ' are ' + str(divisors))
