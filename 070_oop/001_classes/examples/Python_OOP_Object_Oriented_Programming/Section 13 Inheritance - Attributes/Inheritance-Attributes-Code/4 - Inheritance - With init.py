class Vehicle:

    def __init__(self, speed, miles, price):
        self.speed = speed
        self.miles = miles
        self.price = price

class Truck(Vehicle):        

    def __init__(self, speed, miles, price, driver):
        Vehicle.__init__(self, speed, miles, price)
        self.driver = driver
        

class Airplane(Vehicle):

    def __init__(self, speed, miles, price, pilot):
        Vehicle.__init__(self, speed, miles, price)
        self.pilot = pilot
    
        
