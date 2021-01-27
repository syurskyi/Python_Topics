import re

from table import (names, aliases, points, awake,
                   SEPARATOR, generate_table)

# cast to list in case of generator
table1 = list(generate_table(names))
table2 = list(generate_table(names, aliases))
table3 = list(generate_table(names, aliases, points))
table4 = list(generate_table(names, aliases, points, awake))


def test_generate_table():
    a__ len(table1) == len(table2) == len(table3) == len(table4) == 6

    a__ table1[0].count(SEPARATOR) == 0
    a__ table2[0].count(SEPARATOR) == 1
    a__ table3[0].count(SEPARATOR) == 2
    a__ table4[0].count(SEPARATOR) == 3

    a__ table1[1].split(SEPARATOR)[0] == 'Bob'
    a__ table2[1].split(SEPARATOR)[1] == 'Nerd'
    a__ re.match(r'\d+', table3[2].split(SEPARATOR)[2])
    a__ table4[2].split(SEPARATOR)[3]