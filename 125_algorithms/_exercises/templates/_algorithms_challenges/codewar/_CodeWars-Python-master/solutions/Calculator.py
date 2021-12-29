"""
Calculator
http://www.codewars.com/kata/5235c913397cbf2508000048/train/python
"""
_______ operator


class Calculator(object):
    operands = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

    ___ __init__(self):
        self.result    # list

    ___ evaluate(self, string):
        self.result = string.s..(' ')
        self._loop('*/')
        self._loop('+-')
        r.. float(self.result[0])

    ___ _loop(self, operators):
        i = 1
        w.... i < l..(self.result) - 1:
            __ self.result[i] __ operators:
                self.result[i - 1] = s..(self.__class__.operands[self.result[i]](float(self.result[i - 1]), float(self.result[i + 1])))
                self.result.pop(i + 1)
                self.result.pop(i)
                continue
            i += 1
