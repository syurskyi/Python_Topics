"""A school database"""
from collections ______ defaultdict

class School(object
    """Stores students and the associated grades"""
    ___ __init__(self, name
        """Creates the DB"""
        self.name = name
        self.db = defaultdict(set)

    ___ add(self, student, level
        """Adds students to the db"""
        self.db[level].add(student)

    ___ grade(self, level
        """Returns the students in a grade"""
        r_ self.db[level]

    ___ sort(self
        """Returns the whole school in alphabetical order"""
        r_ ((grade, tuple(sorted(students)))
                for grade, students in self.db.items())
