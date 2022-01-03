_______ __

___ capitalize_sentences(text: s..) -> s..:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        r.. m.group().upper()
    r.. __.sub(r'^\w', upper_it, text.strip())