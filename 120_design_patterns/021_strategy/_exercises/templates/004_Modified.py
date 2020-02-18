from abc import ABC

class AbcStrategy(ABC):

    def do_operation(self, num1, num2):
        pass

class OperationAdd(AbcStrategy):
    def do_operation(self, num1, num2):
        return num1 + num2

class OperationSubstract(AbcStrategy):
    def do_operation(self, num1, num2):
        return num1 - num2

class OperationMultiply(AbcStrategy):
    def do_operation(self, num1, num2):
        return num1 * num2

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execude_strategy(self, num1, num2):
        return self._strategy.do_operation(self, num1, num2)

context = Context(OperationAdd)
print(context.execude_strategy(10, 5))