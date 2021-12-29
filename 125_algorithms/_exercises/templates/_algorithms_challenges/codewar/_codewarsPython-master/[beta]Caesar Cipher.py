_______ string
___ caesar(s, shift):
    transDict = {}
    alpha = string.ascii_lowercase
    alphaTrans = alpha[shift:] + alpha[:shift]
    ___ key,value __ z..(string.ascii_lowercase,alphaTrans):
        transDict[key] = value
        transDict[key.upper()] = value.upper()

    r.. ''.join([transDict[c] __ c __ transDict ____ c ___ c __ s])








