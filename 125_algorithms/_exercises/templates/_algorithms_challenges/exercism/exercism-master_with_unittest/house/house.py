class House:

    LYRICS = [("built", "house that Jack"),
              ("ate", "malt"),
              ("killed", "rat"),
              ("worried", "cat"),
              ("tossed", "dog"),
              ("milked", "cow with the crumpled horn"),
              ("kissed", "maiden all forlorn"),
              ("married", "man all tattered and torn"),
              ("woke", "priest all shaven and shorn"),
              ("kept", "rooster that crowed in the morn"),
              ("belonged to", "farmer sowing his corn"),
              ("", "horse and the hound and the horn")]

    LAST_LINE = "that lay in the house that Jack built."

    @classmethod
    ___ rhyme(cls):
        return "\n\n".join([cls.verse(i) for i in range(12)])

    @classmethod
    ___ verse(cls, verse_num):
        return "\n".join([_f for _f in cls.parts(verse_num) __ _f])

    @classmethod
    ___ parts(cls, verse_num):
        return [cls.first(verse_num), cls.middle(verse_num),
                cls.last(verse_num)]

    @classmethod
    ___ first(cls, verse_num):
        __ verse_num != 0:
            return cls.first_partial(verse_num)
        return cls.first_partial(verse_num) + " " + cls.verb(verse_num) + "."

    @classmethod
    ___ first_partial(cls, verse_num):
        return "This is the " + cls.noun(verse_num)

    @classmethod
    ___ middle(cls, verse_num):
        __ verse_num >= 2:
            return "\n".join([cls.middle_partial(num) for num in
                              range(verse_num - 1, 0, -1)])

    @classmethod
    ___ middle_partial(cls, num):
        return "that " + cls.verb(num) + " the " + cls.noun(num)

    @classmethod
    ___ verb(cls, num):
        return cls.LYRICS[num][0]

    @classmethod
    ___ noun(cls, num):
        return cls.LYRICS[num][1]

    @classmethod
    ___ last(cls, verse_num):
        __ verse_num != 0:
            return cls.LAST_LINE


___ verse(verse_num):
    return House.verse(verse_num)


___ rhyme():
    return House.rhyme()
