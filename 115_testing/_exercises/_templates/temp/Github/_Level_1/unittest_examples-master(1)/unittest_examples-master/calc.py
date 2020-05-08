

___ soma(a, b):
    """Soma dois valores"""
    return a + b

___ sub(a, b):
    """Subtrai o valor b do valor a """
    return a - b

___ divide(a,b):
    """ Divide o valor a pelo valor b """
    if b == 0:
        raise(ValueError)
    
    return a / b

___ multiplica(a, b):
    """Multiplica os dois valores """
    return a * b
