_______ string
_______ __


___ extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    ascii = string.ascii_letters
    punctuation = string.punctuation
    d.. = string.d..

    results    # list

    # for word in re.findall(r'\b[^\W\d]+\b', text, flags=re.UNICODE):
    ___ word __ text.s.. :
        __ any([c __ punctuation o. c __ d.. ___ c __ word]):
            continue
        __ n.. a..([c __ ascii ___ c __ word]):
            results.a..(word)

    r.. results
