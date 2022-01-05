c_ Garden(object):

    __plant_names = {"C": "Clover", "G": "Grass",
                     "R": "Radishes", "V": "Violets"}

    ___ - , diagram,
                 students=("Alice Bob Charlie David "
                           "Eve Fred Ginny Harriet "
                           "Ileana Joseph Kincaid Larry").s..()):
        plant_rows = diagram.s..
        students = s..(students)

    ___ plants  student):
        slot_start = students.index(student) * 2
        slot = slice(slot_start, slot_start + 2)
        r.. [__plant_names[abbrev]
                ___ abbrev __ (plant_rows[0][slot] +
                               plant_rows[1][slot])]
