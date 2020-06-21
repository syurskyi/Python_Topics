class House:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getter")
        return self._price

    @price.setter
    def price(self, new_price):
        if self._price > 0:
            self._price = new_price
        else:
            print("Please enter a valid price")

house = House(50000)

print(house.price) # The getter is called

house.price = 60000 # The setter is called

print(house.price) # The value was modified

house.price = -6 # Invalid value

print(house.price) # The value was not modified

