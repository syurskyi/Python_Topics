"""Tracks student plants in a kidnergarden garden"""

class Garden(object
    """Rembers which student has which plant"""
    # Default student list
    students = ["Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
               ]

    # Default plant codes
    plant_codes = {"G": "Grass",
                   "C": "Clover",
                   "R": "Radishes",
                   "V": "Violets",
                  }

    # Default number of cups student has per row
    cups_per_row = 2

    ___ __init__(self, garden, students=None
        """Builds the student garden"""
        __ students:
            self.students = sorted(students)
        # Data structure that holds the garden (dictionary of lists)
        self.student_garden = {}

        # Formats the garden string into rows with groups of cups
        garden = garden.split("\n")
        ___ i, row in enumerate(garden
            garden[i] = [row[j:j+self.cups_per_row] \
                         ___ j in range(0, le.(row), self.cups_per_row)]

        # Assigns columns of cups to students
        ___ student, plants in zip(self.students, zip(*garden)):
            self.student_garden[student] = ''.join(plants)

    ___ plants(self, student
        """Translats the string into plant names and returns"""
        r_ [self.plant_codes[p] ___ p in self.student_garden[student]]
