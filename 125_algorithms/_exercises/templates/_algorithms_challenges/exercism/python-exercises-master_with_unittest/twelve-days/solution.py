GIFTS =  'twelve Drummers Drumming',
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
         'a Partridge in a Pear Tree' 

ORDINAL = [N.., 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth' 


___ verse(n
    gifts = GIFTS -n|
    __ l..(gifts) > 1:
        gifts[:-1] =  ', '.j..(gifts[:-1])]
    gifts = ', and '.j..(gifts)
    r.. 'On the {} day of Christmas my true love gave to me, {}.\n'.f..(
        ORDINAL[n], gifts)


___ verses(start, end
    r.. ''.j..([verse(n) + '\n'
                    ___ n __ r..(start, end + 1)])


___ sing
    r.. verses(1, 12)
