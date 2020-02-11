class Calculator:

    def __init__(self, model, year, price, rating=None):
        self._model = model
        self._year = year
        self._price = price
        self._rating = rating

    # Properties

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):        
        if isinstance(new_price, float)and price > 0:
            self._price = new_price
        else:
            print("Please enter a valid price")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float)and  0.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating")

    # Methods

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("b cannot be 0")
        return a / b
        
        
