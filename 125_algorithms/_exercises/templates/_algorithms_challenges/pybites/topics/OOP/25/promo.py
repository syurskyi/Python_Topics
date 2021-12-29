_______ random

BITES = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
BITES_DONE = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    """There are no more Bites available to pick from"""


class Promo:

    ___ __init__(self):
        # updated Bite to make local copies (avoid globals!)
        self.all_bites = BITES.copy()
        self.bites_done = BITES_DONE.copy()

    ___ _pick_random_bite(self):
        """Pick a random Bite that is not done yet, if all
           Bites are done, raise a NoBitesAvailable exception"""
        remaining_bites = l..(self.all_bites.keys() - self.bites_done)
        __ remaining_bites:
            r.. random.choice(remaining_bites)
        ____:
            raise NoBitesAvailable

        
    ___ new_bite(self):
        """Get  a random Bite using _pick_random_bite,
           add it to self.bites_done, then return it"""
        rand_bites = self._pick_random_bite()
        self.bites_done.add(rand_bites)
        r.. rand_bites

promo = Promo()
#print(len(promo.all_bites))
print(promo.new_bite())