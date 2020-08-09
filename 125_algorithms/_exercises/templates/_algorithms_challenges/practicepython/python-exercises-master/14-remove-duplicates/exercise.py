#! /usr/bin/env python
______ random
______ numpy as np


___ removeDuplicates(list
    result = []
    ___ el in list:
        __ el not in result:
            result.append(el)

    r_ result


__ __name__ __ '__main__':
    list = list(np.random.choice(5, 8, replace=True))
    result = removeDuplicates(list)
    print('List: ' + str(list) + '\nNo dups: ' + str(result))
