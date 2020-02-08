from strategies.strategy import Strategy

class StrategyAlmpl(Strategy):
    def calculate(value):
        return value * 0.03

    def toString(self):
        return 'Strategy A'

