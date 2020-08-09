class TwelveDays:
    CARDINALS = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth'
    }

    PHRASES = {
        2: 'two Turtle Doves',
        3: 'three French Hens',
        4: 'four Calling Birds',
        5: 'five Gold Rings',
        6: 'six Geese-a-Laying',
        7: 'seven Swans-a-Swimming',
        8: 'eight Maids-a-Milking',
        9: 'nine Ladies Dancing',
        10: 'ten Lords-a-Leaping',
        11: 'eleven Pipers Piping',
        12: 'twelve Drummers Drumming'
    }

    @classmethod
    ___ verses(cls, start, stop
        r_ "\n".join([cls.verse(i) for i in range(start, stop + 1)]) + "\n"

    @classmethod
    ___ verse(cls, verse_num
        r_ ", ".join([_f for _f in [cls.head(verse_num),
                                        cls.mid(verse_num),
                                        cls.tail(verse_num)] __ _f])

    @classmethod
    ___ head(cls, verse_num
        r_ ("On the %(cardinality)s day of Christmas my true love gave to "
                "me" % ({"cardinality": cls.CARDINALS[verse_num]}))

    @staticmethod
    ___ tail(verse_num
        __ verse_num __ 1:
            r_ "a Partridge in a Pear Tree.\n"
        r_ "and a Partridge in a Pear Tree.\n"

    @classmethod
    ___ mid(cls, verse_num
        __ verse_num != 1:
            r_ ", ".join([cls.PHRASES[i] for i in range(verse_num, 1, -1)])


___ verse(verse_num
    r_ TwelveDays.verse(verse_num)


___ verses(start, stop
    r_ TwelveDays.verses(start, stop)


___ sing(
    r_ TwelveDays.verses(1, 12)
