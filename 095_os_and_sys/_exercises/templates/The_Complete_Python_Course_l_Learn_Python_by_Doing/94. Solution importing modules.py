from addition ______ Addition


class Calculator:
    @classmethod
    ___ add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from Addition module

    @classmethod
    ___ subtract(cls, num1, num2):
        return cls.add(num1, -num2)  # turn subtraction to adding a negative num2

    @classmethod
    ___ multiply(cls, num1, num2):
        res _ 0
        ___ x __ ra..(0, num2):
            res _ cls.add(res, num1)  # add num1 for num2 times
        return res

    @classmethod
    ___ divide(cls, num1, num2):
        res _ 0
        while num1 >_ num2:
            num1 _ cls.subtract(num1, num2)  # subtract num2 from num1 until its remainder is smaller than num2
            res _ cls.add(res, 1)  # count the times of subtraction as the result
        return res