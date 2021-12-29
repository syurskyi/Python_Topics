____ collections _______ defaultdict


class School(object):
    ___ __init__(self, name):
        self.name = name
        self.db = defaultdict(set)

    ___ add(self, student, grade):
        self.db[grade].add(student)

    ___ grade(self, level):
        r.. self.db[level]

    ___ sort(self):
        r.. s..((grade, tuple(s..(students)))
                      ___ grade, students __ self.db.items())
