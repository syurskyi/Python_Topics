from string import ascii_lowercase


___ is_pangram(sentence):
    return all(char in sentence.lower() for char in ascii_lowercase)
