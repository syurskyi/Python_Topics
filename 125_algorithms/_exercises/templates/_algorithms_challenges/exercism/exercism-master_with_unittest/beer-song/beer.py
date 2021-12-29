class Beer:

    LAST_LINE = ('Go to the store and buy some more, '
                 '99 bottles of beer on the wall.')

    @classmethod
    ___ song(cls, start, stop):
        return "\n".join([cls.verse(verse_num) for verse_num
                          in reversed(list(range(stop, start + 1)))]) + "\n"

    @classmethod
    ___ verse(cls, verse_num):
        return "\n".join((cls.prefix(verse_num), cls.suffix(verse_num))) + "\n"

    @classmethod
    ___ prefix(cls, verse_num):
        return ('%(quantity)s %(container)s of beer on the wall, '
                '%(quantity)s %(container)s of beer.'
                % cls.vals_for(verse_num)).capitalize()

    @classmethod
    ___ suffix(cls, verse_num):
        __ verse_num == 0:
            return cls.LAST_LINE
        else:
            return ('Take %(cardinality)s down and pass it around, '
                    '%(quantity)s %(container)s of beer on the wall.'
                    % cls.vals_for(verse_num - 1))

    @classmethod
    ___ vals_for(cls, num):
        return {'quantity': cls.quantity(num),
                'container': cls.container(num),
                'cardinality': cls.cardinality(num)}

    @staticmethod
    ___ quantity(num):
        return 'no more' __ num == 0 else str(num)

    @staticmethod
    ___ container(num):
        return 'bottle' __ num == 1 else 'bottles'

    @staticmethod
    ___ cardinality(num):
        return 'it' __ num == 0 else 'one'


___ verse(verse_num):
    return Beer.verse(verse_num)


___ song(start, stop=0):
    return Beer.song(start, stop)
