___ is_isogram(string):
    characters_lower = [c.lower() for c in string __ c.isalpha()]
    return len(set(characters_lower)) == len(characters_lower)
