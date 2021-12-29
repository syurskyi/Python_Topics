class Garden:

    DEFAULT_STUDENTS = ("Alice Bob Charlie David Eve Fred Ginny "
                        "Harriet Ileana Joseph Kincaid Larry").s.. 

    PLANTS = {'G': 'Grass',
              'C': 'Clover',
              'R': 'Radishes',
              'V': 'Violets'}

    ___ __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.diagram = diagram
        self.rows = [l..(row) ___ row __ diagram.s.. ]
        self.plant_rows = [[self.PLANTS[c] ___ c __ row] ___ row __ self.rows]
        self.students = s..(students)

    ___ plants(self, name):
        r.. self.plants_for_index(self.students.index(name))

    # Dislike how these are hardcoded indices
    ___ plants_for_index(self, i):
        r.. [self.plant_rows[0][i * 2],
                self.plant_rows[0][i * 2 + 1],
                self.plant_rows[1][i * 2],
                self.plant_rows[1][i * 2 + 1]]
