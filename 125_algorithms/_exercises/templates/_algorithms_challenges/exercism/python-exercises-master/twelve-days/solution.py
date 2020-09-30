GIFTS = ['twelve Drummers Drumming',
         'eleven Pipers Piping',
         'ten Lords-a-Leaping',
         'nine Ladies Dancing',
         'eight Maids-a-Milking',
         'seven Swans-a-Swimming',
         'six Geese-a-Laying',
         'five Gold Rings',
         'four Calling Birds',
         'three French Hens',
         'two Turtle Doves',
         'a Partridge in a Pear Tree']

ORDINAL = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']


___ verse(n
    gifts = GIFTS[-n:]
    __ le.(gifts) > 1:
        gifts[:-1] = [', '.join(gifts[:-1])]
    gifts = ', and '.join(gifts)
    r_ 'On the {} day of Christmas my true love gave to me, {}.\n'.format(
        ORDINAL[n], gifts)


___ verses(start, end
    r_ ''.join([verse(n) + '\n'
                    ___ n __ range(start, end + 1)])


___ sing(
    r_ verses(1, 12)
