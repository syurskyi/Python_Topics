import difflib

___ foo(string1, string2):
    return difflib.SequenceMatcher(N..,string1, string2).ratio()