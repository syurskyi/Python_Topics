from .operations import Multiply, Add, Substract

class MyApp(object):
    def __init__(self):
        self.operations={'multiply': Multiply,
                         'add': Add,
                         'substract': Substract}

    def do(self, operation, number1, number2):
        return self.operations[operation.lower()].do(number1, number2)

