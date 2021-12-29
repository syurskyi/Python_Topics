car_brands = ['Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda']


def convert_to_tuple(car_brands):
    static_cars = tuple(car_brands)
    return static_cars


# Complete this function such that it prints the return value from the convert_to_tuple function
def print_tuples(car_brands):
    car_brands = convert_to_tuple()
    if car_brands:
        print(car_brands)
    return