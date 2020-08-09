______ string
___ caesar(s, shift
    transDict = {}
    alpha = string.ascii_lowercase
    alphaTrans = alpha[shift:] + alpha[:shift]
    ___ key,value in zip(string.ascii_lowercase,alphaTrans
        transDict[key] = value
        transDict[key.upper()] = value.upper()

    r_ ''.join([transDict[c] __ c in transDict else c ___ c in s])








