import difflib

___ foo(string1, string2):
    r_ difflib.SequenceMatcher(None,string1, string2).ratio()