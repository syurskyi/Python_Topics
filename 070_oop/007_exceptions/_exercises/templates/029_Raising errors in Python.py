# Raising errors in Python
#
# NotImplementedError
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
    # print('this method is a  work in progress.') 1.
        raise NotImplementedError("we Can't add cars in to the Garage Yet.")

ford = Garage()
ford.add_car('Fiesta')
print(len(ford))