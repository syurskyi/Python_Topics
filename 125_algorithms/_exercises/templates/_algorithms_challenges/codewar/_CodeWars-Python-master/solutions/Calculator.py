"""
Calculator
http://www.codewars.com/kata/5235c913397cbf2508000048/train/python
"""
_______ operator


c_ Calculator(o..):
    operands = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

    ___ - ):
        result    # list

    ___ evaluate  s__):
        result = s__.s..(' ')
        _loop('*/')
        _loop('+-')
        r.. float(result[0])

    ___ _loop  operators):
        i = 1
        w.... i < l..(result) - 1:
            __ result[i] __ operators:
                result[i - 1] = s..(__class__.operands[result[i]](float(result[i - 1]), float(result[i + 1])))
                result.pop(i + 1)
                result.pop(i)
                _____
            i += 1
