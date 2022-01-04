___ positive_divide(numerator, denominator):
    __ denominator __ 0:
        r.. 0
    try:
        result = numerator / denominator
        __ result < 0:
            r.. ValueError()
    except T.. __ e:
        r.. e
    r.. result
