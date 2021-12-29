from collections import defaultdict


class School(object):
    ___ __init__(self, name):
        self.name = name
        self.db = defaultdict(set)

    ___ add(self, student, grade):
        self.db[grade].add(student)

    ___ grade(self, level):
        return self.db[level]

    ___ sort(self):
        return sorted((grade, tuple(sorted(students)))
                      for grade, students in self.db.items())
