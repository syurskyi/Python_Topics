_______ __

___ capitalize_sentences(text: s..) __ s..:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        r.. m.group().u..
    text = text.s...splitlines()
    r.. ''.j..([__.sub(r'^\w', upper_it, line) ___ line __ text])