c_ House:

    LYRICS [("built", "house that Jack"),
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

    LAST_LINE "that lay in the house that Jack built."

    ??
    ___ rhyme(cls
        r.. "\n\n".j..([cls.verse(i) ___ i __ r..(12)])

    ??
    ___ verse(cls, verse_num
        r.. "\n".j..([_f ___ _f __ cls.parts(verse_num) __ _f])

    ??
    ___ parts(cls, verse_num
        r.. [cls.first(verse_num), cls.middle(verse_num),
                cls.last(verse_num)]

    ??
    ___ first(cls, verse_num
        __ verse_num !_ 0:
            r.. cls.first_partial(verse_num)
        r.. cls.first_partial(verse_num) + " " + cls.verb(verse_num) + "."

    ??
    ___ first_partial(cls, verse_num
        r.. "This is the " + cls.noun(verse_num)

    ??
    ___ middle(cls, verse_num
        __ verse_num >_ 2:
            r.. "\n".j..([cls.middle_partial(num) ___ num __
                              r..(verse_num - 1, 0, -1)])

    ??
    ___ middle_partial(cls, num
        r.. "that " + cls.verb(num) + " the " + cls.noun(num)

    ??
    ___ verb(cls, num
        r.. cls.LYRICS[num][0]

    ??
    ___ noun(cls, num
        r.. cls.LYRICS[num][1]

    ??
    ___ last(cls, verse_num
        __ verse_num !_ 0:
            r.. cls.LAST_LINE


___ verse(verse_num
    r.. House.verse(verse_num)


___ rhyme
    r.. House.rhyme()
