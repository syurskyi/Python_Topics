import types

class StrategyExample:
    def __init__(self, func=None):
        self.name = 'Default Strategy'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()
    strat0.execute()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'
    strat1.execute()

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'
    strat2.execute()
