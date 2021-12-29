import unicodedata
___ filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    text = text.lower()
    result = []
    

    s = unicodedata.normalize('NFD',text).encode("ascii",'ignore').decode('utf-8')
    for character_1,character_2 in zip(text,s):
        __ character_1 != character_2:
            result.append(character_1)


    return result

