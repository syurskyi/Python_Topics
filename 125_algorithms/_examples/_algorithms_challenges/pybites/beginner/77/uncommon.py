def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    #print(my_cities + other_cities)
    #print(set(my_cities) ^ set(other_cities))
    return len(set(my_cities) ^ set(other_cities))



my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']

#print(len(my_cities))

print( uncommon_cities(my_cities, other_cities) )