_______ p__

____ identity_and_equality _______ (
    Car,
    is_same_car_color_and_model,
    is_same_instance_of_car,
)


# `NewList` for tests
c_ NewList(l..):
    p..


# A bunch of lists to test
l1 = [["gas", "electro", "hybrid"], "200 PS", "radio"]
l2 = l1
l3 = l1.c..
l4 = l1[0]
l5 = [l4, "digital radio"]
l6 = [l1[0], "digital radio"]
l7 = NewList(l1)
l8 = ["unleaded"]

# A bunch of `Car`s
my_car = Car("Toyota Corolla", "black")
other_car1 = my_car
other_car2 = Car("Toyota Corolla", "black")
other_car3 = Car("Toyota Corolla", "red")
other_car4 = Car("Porsche Cayenne", "black")


# Test staticmethod Car.age
?p__.m__.p.(
    "days, expected",
    [
        (7, "A week old"),  # week
        (365, "A year old"),  # year
        (2, "Neither a week, nor a year old"),  # Other number
    ],
)
___ test_car_age(days, expected):
    ... Car.age(days) __ expected


# Test staticmethod Car.age
?p__.m__.p.(
    "list1, list2, expected",
    [
        ([], [], T..),  # Empty
        (l1, l2, T..),  # same instance
        (l1, l1 | , T..),  # full copy
        (l1, l3, T..),  # full copy
        (l5, l6, T..),  # Two identical short lists
        (l5[0], l6[0], T..),  # First element of short lists (same instances)
        (l1, l7, T..),  # One list, one NewList, same contents
        #(l1, l8, False),  # Two completely different lists
    ],
)
___ test_the_same_configuration(list1, list2, expected):
    ... Car.has_same_configuration(list1, list2) __ expected


?p__.m__.p.(
    "car1, car2, expected",
    [
        (my_car, my_car, T..),  # Identical cars (same instance)
        (my_car, other_car1, T..),  # Identical cars (same instance)
        (my_car, other_car2, T..),  # Car of the same model and color
        (other_car2, other_car3, F..),  # Completely different cars
    ],
)
___ test_is_same_car_color_and_model(car1, car2, expected):
    ... is_same_car_color_and_model(car1, car2) __ expected


?p__.m__.p.(
    "car1, car2, expected",
    [
        (my_car, my_car, T..),  # Same instance
        (my_car, other_car1, T..),  # Same Car, different instance
        (other_car1, other_car2, F..),  # Completely different cars
    ],
)
___ test_is_the_same_instance_of_car(car1, car2, expected):
    ... is_same_instance_of_car(car1, car2) __ expected
