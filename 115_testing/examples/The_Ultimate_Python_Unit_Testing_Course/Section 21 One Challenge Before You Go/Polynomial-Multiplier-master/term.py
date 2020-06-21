class Term:
    def __init__(self, coefficient, power):
        self._coefficient = coefficient
        self._power = power

    def get_power(self):
        return self._power

    def get_coefficient(self):
        return self._coefficient
