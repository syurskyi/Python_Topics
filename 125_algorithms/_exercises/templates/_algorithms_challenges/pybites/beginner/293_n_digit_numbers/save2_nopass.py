car_brands = ['Mazda', 'McLaren', 'Opel', 'Toyota', 'Honda']


___ convert_to_tuple(car_brands):
    static_cars = tuple(car_brands)
    return static_cars


# Complete this function such that it prints the return value from the convert_to_tuple function
___ print_tuples(car_brands):
    car_brands = convert_to_tuple()
    return print(car_brands)