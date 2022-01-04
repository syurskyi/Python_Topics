_______ __

___ capitalize_sentences(text: s..) -> s..:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        r.. m.group().u..
    sentence = __.s..(r'([!?.])\s', text)
    output = ' '.j..([__.sub(r'^\w', upper_it, line) ___ line __ sentence])
    r.. __.sub(r'\s([?.!])', r'\1', output)