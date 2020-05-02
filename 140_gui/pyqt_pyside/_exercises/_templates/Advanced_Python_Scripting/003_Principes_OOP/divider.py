c_ dividerClass(object
    ___  -  
        __div = 1

    ___ divide , value
        return value / __div

    ___ setDivider , val
        __ __checkValue(val
            __div = val
        else:
            print 'Wrong value'

    ___ __checkValue , val
        return not val __ 0

d = dividerClass()
d.setDivider(2)
d.divide(100)
