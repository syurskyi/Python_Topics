c_ dividerClass(object
    ___  -  
        __div _ 1

    ___ divide , value
        return value / __div

    ___ setDivider , val
        __ __checkValue(val
            __div _ val
        else:
            print 'Wrong value'

    ___ __checkValue , val
        return not val __ 0

d _ dividerClass()
d.setDivider(2)
d.divide(100)
