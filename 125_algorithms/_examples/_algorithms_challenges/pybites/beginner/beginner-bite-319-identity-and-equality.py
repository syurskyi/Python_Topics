"""
Identity and equality are two important concepts in Python.
Please correct the mistakes in the Car class (marked with # *) and and complete the functions below.

Use the errors in the tests as guidance to what needs fixing.
The Car class has two static functions that should behave in the following way:

>>> Car.age(1)
'Neither a week, nor a year old'
>>> Car.age(7)
'A week old'
>>> Car.age(365)
'A year old'

>>> config1 = ["manual", "radio"]
>>> config2 = ["manual", "radio"]
>>> config3 = ["manual"]

>>> Car.has_same_configuration(config1, config2)
True
>>> Car.has_same_configuration(config1, config3)
False
Please also complete the two functions is_same_car_color_and_model and
is_same_instance_of_car to behave like this:

>>> car1 = Car("Pickup", "black")
>>> car2 = Car("Pickup", "black")
>>> car3 = car1
>>> is_same_car_color_and_model(car1, car2)
True
>>> is_same_car_color_and_model(car1, car3)
True
>>> is_same_instance_of_car(car1, car2)
False
>>> is_same_instance_of_car(car1, car3)
True

Check out the articles below for additional pointers to solve the bite:

- Python '!=' Is Not 'is not'

- What are the differences between type() and isinstance()?
"""

# TODO: Fix age and same_configuration functions (see test results)
class Car:
    """
    Car class
    -> Have a closer look at lines marked with '# *'
    """

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __eq__(self, other_car):
        return (
            self.model.lower() == other_car.model.lower()
            and self.color.lower() == other_car.color.lower()
        )

    @staticmethod
    def age(days):
        """if / elif / else for exercise sake, if there would
           be more conditions we would use a dict / mapping
        """
        if days is 7:  # *
            return "A week old"
        elif days is 365:  # *
            return "A year old"
        else:
            return "Neither a week, nor a year old"

    @staticmethod
    def has_same_configuration(config1, config2):
        if type(config1) != list or type(config2) != list:  # *
            raise TypeError()
        return config1 is config2  # *


# TODO: Complete function
def is_same_car_color_and_model(car1, car2):
    """
    Returns true if car1 and car2 are the of same model and color
    """
    if car1.__eq__(car2):
        return True
    else:
        return False


# TODO: Complete function
def is_same_instance_of_car(car1, car2):
    """
    Returns true if car1 and car2 are exactly the same object (instance)
    """
    if car1 is car2:
        return True
    else:
        return false


config1 = {}
config2 = [['gas', 'electro', 'hybrid'], '200 PS', 'radio']

if type(config1) != list or type(config2) != list:
    raise TypeError()
else:
    print("OK")

if isinstance(config1, list):
    print("IsInstance OK")
