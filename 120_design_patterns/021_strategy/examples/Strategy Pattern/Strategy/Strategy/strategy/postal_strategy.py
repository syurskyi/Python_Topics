from strategies.strategy import AbsStrategy

class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00