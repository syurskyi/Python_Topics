class Calculator:
    
    def __init__(self, model, year):
        self.model = model
        self.year = year

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

my_calculator = Calculator("XM-45", "2019")

# Calling the methods and printing the value returned
print(my_calculator.add(5, 4))
print(my_calculator.subtract(8, 2))
print(my_calculator.multiply(3, 5))
print(my_calculator.divide(6, 2))

# These calls will raise a ValueError
# print(my_calculator.subtract(2, 8))
print(my_calculator.divide(3, 0))

