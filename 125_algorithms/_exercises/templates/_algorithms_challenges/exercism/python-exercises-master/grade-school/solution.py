from collections ______ defaultdict


class School(object
    ___ __init__(self, name
        self.name = name
        self.db = defaultdict(set)

    ___ add(self, student, grade
        self.db[grade].add(student)

    ___ grade(self, level
        r_ self.db[level]

    ___ sort(self
        r_ sorted((grade, tuple(sorted(students)))
                      for grade, students in self.db.items())
