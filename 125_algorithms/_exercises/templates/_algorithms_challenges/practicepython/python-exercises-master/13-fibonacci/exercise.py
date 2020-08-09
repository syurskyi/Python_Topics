#! /usr/bin/env python

___ generateFibbonaci(length
    list = [1,1]

    ___ x in range(1, length - 1
        list.append(list[x-1] + list[x])

    r_ list

__ __name__ __ '__main__':
    number = int(raw_input('How many fibonaccies ? '))
    result = generateFibbonaci(number)
    print('The fibonaccies are: ' + str(result))
