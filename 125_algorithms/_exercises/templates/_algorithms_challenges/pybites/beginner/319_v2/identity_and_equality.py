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
        __ n.. isi..(config1,l..) o. n.. isi..(config2,l..):  # *
            print(type(config1),type(config2))
            raise TypeError()
        r.. config1 __ config2  # *


# TODO: Complete function
___ is_same_car_color_and_model(car1, car2):
    """
    Returns true if car1 and car2 are the of same model and color
    """
    r.. car1 __ car2


# TODO: Complete function
___ is_same_instance_of_car(car1, car2):
    """
    Returns true if car1 and car2 are exactly the same object (instance)
    """
    r.. car1 __ car2
