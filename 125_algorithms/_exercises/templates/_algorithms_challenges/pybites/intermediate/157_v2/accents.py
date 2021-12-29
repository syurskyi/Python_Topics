_______ unicodedata
___ filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    text = text.lower()
    result    # list
    

    s = unicodedata.normalize('NFD',text).encode("ascii",'ignore').decode('utf-8')
    ___ character_1,character_2 __ zip(text,s):
        __ character_1 != character_2:
            result.a..(character_1)


    r.. result

