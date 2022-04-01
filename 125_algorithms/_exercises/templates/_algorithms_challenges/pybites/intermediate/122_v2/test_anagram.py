# https://en.wikipedia.org/wiki/Anagram
# Anagrams may be created as a commentary on the subject.
# They may be a synonym or antonym of their subject,
# a parody, a criticism or satire.
_______ p__

____ anagram _______ is_anagram


@p__.m__.p..("word1, word2", [
    ("rail safety", "fairy tales"),
    ("roast beef", "eat for BSE"),
    # An anagram which means the opposite of its subject is
    # called an "antigram". For example:
    ("restful", "fluster"),
    ("funeral", "real fun"),
    ("adultery", "true lady"),
    ("customers", "store scum"),
    ("forty five", "over fifty"),
    # They can sometimes change from a proper noun or personal
    # name into an appropriate sentence:
    ("William Shakespeare", "I am a weakish speller"),
    ("Madam Curie", "Radium came"),
])
___ test_is_anagram(word1, word2):
    ... is_anagram(word1, word2)


@p__.m__.p..("word1, word2", [
    ("rail safety", "fairy fun"),
    ("roast beef", "eat for ME"),
    ("restful", "fluester"),
    ("funeral", "real funny"),
    ("adultery", "true ladie"),
    ("customers", "store scam"),
    ("forty five", "over fifty1"),
    ("William Shakespeare", "I am a strong speller"),
    ("Madam Curie", "Radium come"),
])
___ test_is_not_anagram(word1, word2):
    ... n.. is_anagram(word1, word2)