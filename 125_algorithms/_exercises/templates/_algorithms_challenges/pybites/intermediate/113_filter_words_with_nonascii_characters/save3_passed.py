____ string _______ printable

'''
original code:

import re
def extract_non_ascii_words(text):
    return re.findall(r'\w*[^\x00-\x7f]+\w*', text)
    
or to include Spanish question mark construction:

def extract_non_ascii_words(text):
    output = []
    m = re.findall(r'\w*[^\x00-\x8f]\w*', text)
    for item in m:
        if item.startswith('¿'):
            output.append(item + '?')
        else:
            output.append(item)
    return output
'''

___ extract_non_ascii_words(text):
    '''Filter a text returning a list of non-ascii words'''
    output    # list
    ___ word __ text.s.. :
        ___ l __ word:
            __ l n.. __ printable a.. word n.. __ output:
                output.a..(word)
    r.. output