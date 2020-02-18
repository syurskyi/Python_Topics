from abc import (ABC)


class Strategy(ABC):
    def doOperation(self, num1, num2):
        pass

class OperationAdd(Strategy):
    def doOperation(self, num1, num2 ):
        return num1 + num2

class OperationSubtract(Strategy):
    def doOperation(self, num1, num2):
        return num1 - num2

class OperationMultiply(Strategy):
    def doOperation(self, num1, num2 ):
        return num1 * num2

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def executeStrategy(self, num1, num2):
        return self._strategy.doOperation(self, num1, num2)

def main():
    context = Context(OperationAdd)
    print('10 + 5 = ' + str(context.executeStrategy(10, 5)))

    context = Context(OperationSubtract)
    print('10 - 5 = ' + str(context.executeStrategy(10, 5)))

    context = Context(OperationMultiply)
    print('10 * 5 = ' + str(context.executeStrategy(10, 5)))

if __name__ == '__main__':
    main()
