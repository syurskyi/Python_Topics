c_ Beer:

    LAST_LINE = ('Go to the store and buy some more, '
                 '99 bottles of beer on the wall.')

    @classmethod
    ___ song(cls, start, stop):
        r.. "\n".j..([cls.verse(verse_num) ___ verse_num
                          __ reversed(l..(r..(stop, start + 1)))]) + "\n"

    @classmethod
    ___ verse(cls, verse_num):
        r.. "\n".j..((cls.prefix(verse_num), cls.suffix(verse_num))) + "\n"

    @classmethod
    ___ prefix(cls, verse_num):
        r.. ('%(quantity)s %(container)s of beer on the wall, '
                '%(quantity)s %(container)s of beer.'
                % cls.vals_for(verse_num)).capitalize()

    @classmethod
    ___ suffix(cls, verse_num):
        __ verse_num __ 0:
            r.. cls.LAST_LINE
        ____:
            r.. ('Take %(cardinality)s down and pass it around, '
                    '%(quantity)s %(container)s of beer on the wall.'
                    % cls.vals_for(verse_num - 1))

    @classmethod
    ___ vals_for(cls, num):
        r.. {'quantity': cls.quantity(num),
                'container': cls.container(num),
                'cardinality': cls.cardinality(num)}

    @staticmethod
    ___ quantity(num):
        r.. 'no more' __ num __ 0 ____ s..(num)

    @staticmethod
    ___ container(num):
        r.. 'bottle' __ num __ 1 ____ 'bottles'

    @staticmethod
    ___ cardinality(num):
        r.. 'it' __ num __ 0 ____ 'one'


___ verse(verse_num):
    r.. Beer.verse(verse_num)


___ song(start, stop=0):
    r.. Beer.song(start, stop)
