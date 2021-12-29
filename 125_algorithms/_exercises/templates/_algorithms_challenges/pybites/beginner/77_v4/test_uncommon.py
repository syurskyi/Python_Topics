____ Previous.uncommon _______ uncommon_cities


___ test_uncommon_part_overlap():
    my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
    other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']
    ... uncommon_cities(my_cities, other_cities) __ 8


___ test_uncommon_all_same():
    my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
    other_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
    ... uncommon_cities(my_cities, other_cities) __ 0


___ test_uncommon_all_different():
    my_cities = ['Rome', 'Paris', 'Madrid']
    other_cities = ['Chicago', 'Seville', 'Berlin']
    ... uncommon_cities(my_cities, other_cities) __ 6