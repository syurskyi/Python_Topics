c_ Garden:

    DEFAULT_STUDENTS = ("Alice Bob Charlie David Eve Fred Ginny "
                        "Harriet Ileana Joseph Kincaid Larry").s.. 

    PLANTS = {'G': 'Grass',
              'C': 'Clover',
              'R': 'Radishes',
              'V': 'Violets'}

    ___ - , diagram, students=DEFAULT_STUDENTS
        diagram = diagram
        rows = [l..(row) ___ row __ diagram.s.. ]
        plant_rows = [[PLANTS[c] ___ c __ row] ___ row __ rows]
        students = s..(students)

    ___ plants  name
        r.. plants_for_index(students.index(name))

    # Dislike how these are hardcoded indices
    ___ plants_for_index  i
        r.. [plant_rows[0][i * 2],
                plant_rows[0][i * 2 + 1],
                plant_rows[1][i * 2],
                plant_rows[1][i * 2 + 1]]
