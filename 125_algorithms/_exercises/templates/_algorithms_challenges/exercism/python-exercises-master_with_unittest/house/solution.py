parts = [('lay in', 'the house that Jack built'),
         ('ate', 'the malt'),
         ('killed', 'the rat'),
         ('worried', 'the cat'),
         ('tossed', 'the dog'),
         ('milked', 'the cow with the crumpled horn'),
         ('kissed', 'the maiden all forlorn'),
         ('married', 'the man all tattered and torn'),
         ('woke', 'the priest all shaven and shorn'),
         ('kept', 'the rooster that crowed in the morn'),
         ('belonged to', 'the farmer sowing his corn'),
         ('', 'the horse and the hound and the horn')]


___ verse(n):
    v = ['This is {}'.format(parts[n][1])]
    v.extend(['that {0} {1}'.format(parts[i][0], parts[i][1])
              ___ i __ r..(n - 1, -1, -1)])
    v[-1] += '.'
    r.. '\n'.join(v)


___ rhyme():
    r.. "\n\n".join(verse(n) ___ n __ r..(l..(parts)))
