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

    ___ __init__(self, model, color):
        self.model = model
        self.color = color

    ___ __eq__(self, other_car):
        r.. (
            self.model.lower() __ other_car.model.lower()
            and self.color.lower() __ other_car.color.lower()
        )

    @staticmethod
    ___ age(days):
        """if / elif / else for exercise sake, if there would
           be more conditions we would use a dict / mapping
        """
        __ days __ 7:  # *
            r.. "A week old"
        ____ days __ 365:  # *
            r.. "A year old"
        ____:
            r.. "Neither a week, nor a year old"

    @staticmethod
    ___ has_same_configuration(config1, config2):
        __ type(config1) != l.. o. type(config2) != l..:  # *
            raise TypeError()
        r.. config1 __ config2  # *


# TODO: Complete function
___ is_same_car_color_and_model(car1, car2):
    """
    Returns true if car1 and car2 are the of same model and color
    """
    __ car1.__eq__(car2):
        r.. True
    ____:
        r.. False


# TODO: Complete function
___ is_same_instance_of_car(car1, car2):
    """
    Returns true if car1 and car2 are exactly the same object (instance)
    """
    __ car1 __ car2:
        r.. True
    ____:
        r.. false


config1 = {}
config2 = [['gas', 'electro', 'hybrid'], '200 PS', 'radio']

__ type(config1) != l.. o. type(config2) != l..:
    raise TypeError()
____:
    print("OK")

__ isi..(config1, l..):
    print("IsInstance OK")
