ALPHABET = 'abcdefghijklmnopqrstuvwxyz '


___ is_pangram(s):
    return set(list(s.lower())) >= set(ALPHABET)
