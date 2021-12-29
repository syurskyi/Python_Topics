class Garden(object):

    __plant_names = {"C": "Clover", "G": "Grass",
                     "R": "Radishes", "V": "Violets"}

    ___ __init__(self, diagram,
                 students=("Alice Bob Charlie David "
                           "Eve Fred Ginny Harriet "
                           "Ileana Joseph Kincaid Larry").split()):
        self.plant_rows = diagram.s..
        self.students = s..(students)

    ___ plants(self, student):
        slot_start = self.students.index(student) * 2
        slot = slice(slot_start, slot_start + 2)
        r.. [self.__plant_names[abbrev]
                ___ abbrev __ (self.plant_rows[0][slot] +
                               self.plant_rows[1][slot])]
