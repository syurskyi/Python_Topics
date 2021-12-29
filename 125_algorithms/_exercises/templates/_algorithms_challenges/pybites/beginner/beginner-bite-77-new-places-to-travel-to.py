'''
You want to find people who have as much exposure to different cultures as yourself.

Complete the uncommon_cities helper that takes the cities you have visited (my_cities) and the cities the other person
has visited (other_cities) and returns the number of cities that both sequences do NOT have in common.

So given [A B C] and [B C D] it should return 2 because only A and D are different.

You can loop through both sequences but maybe there is a more concise way to do it?
'''

# https://stackoverflow.com/questions/22736641/xor-on-two-lists-in-python
# https://docs.python.org/3/tutorial/datastructures.html

___ uncommon_cities_solution_1(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    result = set(my_cities).symmetric_difference(other_cities)
    r.. l..(result)

uncommon_cities(['A','B','C'], ['A','B','C','D'])

___ uncommon_cities_solution_2(my_cities, other_cities):
    uncommon    # list
    ___ item __ my_cities:
        __ item n.. __ other_cities:
            uncommon.a..(item)
    ___ item __ other_cities:
        __ item n.. __ my_cities:
            uncommon.a..(item)
    r.. l..(uncommon)

___ uncommon_cities_solution_3(my_cities, other_cities):
    r..(l..([a ___ a __ my_cities + other_cities __ (a n.. __ my_cities) o. (a n.. __ other_cities)]))

print(uncommon_cities_solution_1(['A','B','C'], ['A','B','C','D']))
print(uncommon_cities_solution_2(['A', 'B', 'C'], ['A', 'B', 'C', 'D']))
print(uncommon_cities_solution_3(['A', 'B', 'C'], ['A', 'B', 'C', 'D']))