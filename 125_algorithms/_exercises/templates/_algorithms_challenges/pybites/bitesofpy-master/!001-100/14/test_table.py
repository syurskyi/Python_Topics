______ re

from table ______ (names, aliases, points, awake,
                   SEPARATOR, generate_table)

# cast to list in case of generator
table1 = list(generate_table(names))
table2 = list(generate_table(names, aliases))
table3 = list(generate_table(names, aliases, points))
table4 = list(generate_table(names, aliases, points, awake))


___ test_generate_table(
    assert le.(table1) __ le.(table2) __ le.(table3) __ le.(table4) __ 6

    assert table1[0].count(SEPARATOR) __ 0
    assert table2[0].count(SEPARATOR) __ 1
    assert table3[0].count(SEPARATOR) __ 2
    assert table4[0].count(SEPARATOR) __ 3

    assert table1[1].split(SEPARATOR)[0] __ 'Bob'
    assert table2[1].split(SEPARATOR)[1] __ 'Nerd'
    assert re.match(r'\d+', table3[2].split(SEPARATOR)[2])
    assert table4[2].split(SEPARATOR)[3]