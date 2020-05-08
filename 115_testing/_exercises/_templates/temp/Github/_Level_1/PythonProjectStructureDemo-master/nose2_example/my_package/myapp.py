from .operations import Multiply, Add, Substract

c_ MyApp(object):
    ___  - (self):
        self.operations={'multiply': Multiply,
                         'add': Add,
                         'substract': Substract}

    ___ do  operation, number1, number2):
        return self.operations[operation.lower()].do(number1, number2)

