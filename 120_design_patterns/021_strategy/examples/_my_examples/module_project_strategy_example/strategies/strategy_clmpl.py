from strategies.strategy import Strategy

class StrategyClmpl(Strategy):
    def calculate(value):
        return value * 0.1

    def toString(self):
        return 'Strategy C'