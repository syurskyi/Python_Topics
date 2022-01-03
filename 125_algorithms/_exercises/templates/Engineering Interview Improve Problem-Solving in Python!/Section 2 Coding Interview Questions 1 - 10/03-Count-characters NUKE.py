# aabsbddb ... a = 2, b = 3, s = 1, d = 2

___ count_characters(s):
    result  {}
    ___ c __ s:
        result[c]  result.get(c, 0) + 1
    ___ key, value __ result.i..:
        print(key, value)
    #return result

count_characters('aabsbddb')