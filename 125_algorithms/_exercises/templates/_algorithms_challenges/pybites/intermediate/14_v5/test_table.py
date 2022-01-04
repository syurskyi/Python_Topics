_______ __

____ table _______ (names, aliases, points, awake,
                   SEPARATOR, generate_table)

# cast to list in case of generator
table1 = l..(generate_table(names))
table2 = l..(generate_table(names, aliases))
table3 = l..(generate_table(names, aliases, points))
table4 = l..(generate_table(names, aliases, points, awake))


___ test_generate_table():
    ... l..(table1) __ l..(table2) __ l..(table3) __ l..(table4) __ 6

    ... table1[0].c.. SEPARATOR) __ 0
    ... table2[0].c.. SEPARATOR) __ 1
    ... table3[0].c.. SEPARATOR) __ 2
    ... table4[0].c.. SEPARATOR) __ 3

    ... table1[1].s..(SEPARATOR)[0] __ 'Bob'
    ... table2[1].s..(SEPARATOR)[1] __ 'Nerd'
    ... __.m..(r'\d+', table3[2].s..(SEPARATOR)[2])
    ... table4[2].s..(SEPARATOR)[3]