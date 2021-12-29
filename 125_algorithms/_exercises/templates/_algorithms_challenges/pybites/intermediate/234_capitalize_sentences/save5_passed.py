_______ re

___ capitalize_sentences(text: s..) -> s..:
    '''Returns sentence with correct capitalisation.'''
    ___ upper_it(m):
        r.. m.group().upper()
    sentence = re.s..(r'([!?.])\s', text)
    output = ' '.join([re.sub(r'^\w', upper_it, line) ___ line __ sentence])
    r.. re.sub(r'\s([?.!])', r'\1', output)