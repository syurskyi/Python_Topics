class Calculator:
    
    def __init__(self, model, year, serial_num):
        self.model = model
        self.year = year
        self._serial_num = serial_num

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        if a >= b:
            return a - b
        else:
            raise ValueError("a is smaller than b")

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("The denominator (b) cannot be 0")
