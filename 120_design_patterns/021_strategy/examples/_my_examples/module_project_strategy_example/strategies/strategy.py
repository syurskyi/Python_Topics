from abc import ABC


class Strategy(ABC):
    def calculate(self, value):
        pass