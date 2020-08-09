#! /usr/bin/env python
______ numpy as np


___ binarySearch(element, list
    currentIndex = le.(list) / 2
    __ currentIndex < 2:
        print('Element is not in the list :/')
    ____ element < list[currentIndex]:
        binarySearch(element, list[0:currentIndex])
    ____ element > list[currentIndex]:
        binarySearch(element, list[currentIndex:le.(list) - 1])
    ____ element __ list[currentIndex]:
        print('Element is in the list!')


__ __name__ __ '__main__':
    list = list(np.random.choice(100, 20, replace=True))
    list.sort()
    print(str(list))
    number = int(input('Look for: '))
    binarySearch(number, list)
