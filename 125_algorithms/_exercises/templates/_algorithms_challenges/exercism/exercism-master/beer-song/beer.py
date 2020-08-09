class Beer:

    LAST_LINE = ('Go to the store and buy some more, '
                 '99 bottles of beer on the wall.')

    @classmethod
    ___ song(cls, start, stop
        r_ "\n".join([cls.verse(verse_num) ___ verse_num
                          in reversed(list(range(stop, start + 1)))]) + "\n"

    @classmethod
    ___ verse(cls, verse_num
        r_ "\n".join((cls.prefix(verse_num), cls.suffix(verse_num))) + "\n"

    @classmethod
    ___ prefix(cls, verse_num
        r_ ('%(quantity)s %(container)s of beer on the wall, '
                '%(quantity)s %(container)s of beer.'
                % cls.vals_for(verse_num)).capitalize()

    @classmethod
    ___ suffix(cls, verse_num
        __ verse_num __ 0:
            r_ cls.LAST_LINE
        ____
            r_ ('Take %(cardinality)s down and pass it around, '
                    '%(quantity)s %(container)s of beer on the wall.'
                    % cls.vals_for(verse_num - 1))

    @classmethod
    ___ vals_for(cls, num
        r_ {'quantity': cls.quantity(num),
                'container': cls.container(num),
                'cardinality': cls.cardinality(num)}

    @staticmethod
    ___ quantity(num
        r_ 'no more' __ num __ 0 else str(num)

    @staticmethod
    ___ container(num
        r_ 'bottle' __ num __ 1 else 'bottles'

    @staticmethod
    ___ cardinality(num
        r_ 'it' __ num __ 0 else 'one'


___ verse(verse_num
    r_ Beer.verse(verse_num)


___ song(start, stop=0
    r_ Beer.song(start, stop)
