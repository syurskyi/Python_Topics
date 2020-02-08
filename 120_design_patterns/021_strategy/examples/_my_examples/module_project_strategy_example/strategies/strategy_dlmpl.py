from strategies.strategy import Strategy

class StrategyDlmpl(Strategy):
    def calculate(value):
        return (value * 0.1) + 10.0

    def toString(self):
        return 'Strategy D'