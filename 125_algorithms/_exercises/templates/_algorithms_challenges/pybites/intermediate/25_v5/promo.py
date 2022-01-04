_______ r__

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
bites_done = {6, 10, 16, 18, 21}


c_ NoBitesAvailable(Exception):
    p..


c_ Promo:

    ___ - , bites_done=bites_done):
        bites_done = bites_done

    ___ _pick_random_bite
        bites_available = [x ___ x, _ __ BITES.i.. __ x n.. __ bites_done]
        __ l..(bites_available) < 1:
            r.. NoBitesAvailable
        r.. r__.choice(bites_available)

    ___ new_bite
        picked = _pick_random_bite()
        bites_done.add(picked)
        r.. BITES[picked]
