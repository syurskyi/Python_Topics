_______ __

___ extract_non_ascii_words(text
    '''Filter a text returning a list of non-ascii words'''
    r.. __.f..(r'\w*[^\x00-\x7f]+\w*', text)