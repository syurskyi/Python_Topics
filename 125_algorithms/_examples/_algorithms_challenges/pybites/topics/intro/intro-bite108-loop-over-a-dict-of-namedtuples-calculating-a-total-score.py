'''
Bite 108. Loop over a dict of namedtuples calculating a total score
In this Bite you calculate the total amount of points earned with Ninja Belts by accessing the given ninja_belts dict.

You learn how to access score and ninjas (= amount of belt owners) from no less than a namedtuple.

Why a namedtuple, you did not even mention a tuple yet?!

Good point, well in our Bites we might actually use them even more so let's get to know them here
(if you have a free evening read up on the collections module as well and thank us later).

The function returns the total score int. You learn to write generic code because we test for an
updated ninja_belts dict as well, see the TESTS tab.
'''


from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}

def get_total_points(belts=ninja_belts):
    """Calculate the amount of points rewarded on PyBites given the
       ninja_belts dictionary, formula: belt score x belt owners (aka ninjas)
       (of course there are more points but let's keep it simple)

       Make your code generic so if we update ninja_belts to include
       more belts (which we do in the tests) it will still work.

       Ah and you can get score and ninjas from the namedtuple with nice
       attribute access: belt.score / belt.ninjas (reason why we get
       you familiar with namedtuple here, because we love them and use
       them all over the place!)

       Return the total number of points int from the function."""
    values = belts.values()
    total = 0
    for item in values:
        total += item.ninjas * item.score
    return total
print(get_total_points(ninja_belts))