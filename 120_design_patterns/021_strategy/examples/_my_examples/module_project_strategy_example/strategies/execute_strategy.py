class ExecuteStrategy:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute(self, value):
        self.result = self._strategy.calculate(value)

        self.printResult(self.result)

    def printResult(self, result):
        print('Result of ' + str(self._strategy) + 'is: ' + str(self.result))