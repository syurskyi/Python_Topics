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
BITES_DONE = {6, 10, 16, 18, 21}


c_ NoBitesAvailable(E..):
    p..


c_ Promo:

    ___ - ):
        # updated Bite to make local copies (avoid globals!)
        all_bites = BITES.c..
        bites_done = BITES_DONE.c..
    

    $
    ___ all_bites_done
        r.. l..(all_bites) __len(bites_done)
    ___ _pick_random_bite
        """Pick a random Bite that is not done yet, if all
           Bites are done, raise a NoBitesAvailable exception"""
        __ all_bites_done:
            r.. NoBitesAvailable
        r.. r__.choice([key ___ key __ BITES.k.. __ key n.. __ bites_done])

    ___ new_bite
        """Get  a random Bite using _pick_random_bite,
           add it to self.bites_done, then return it"""
        bite = _pick_random_bite()

        bites_done.add(bite)

        r.. bite

        
