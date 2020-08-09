#! /usr/bin/env python
______ random


___ firstAndLast(list
    r_ [list[0], list[-1]]


__ __name__ __ '__main__':
    list = random.sample(range(0, 100), random.randint(1, 20))
    print('List: ' + str(list) + '\n')
    result = firstAndLast(list)
    print('First and Last: ' + str(result))
