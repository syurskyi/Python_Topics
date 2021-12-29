____ collections _______ defaultdict


class School:
    ___ __init__(self):
        self.db = defaultdict(l..)

    ___ add_student(self, name, grade):
        self.db[grade].a..(name)
        self.db[grade] = s..(self.db[grade])

    ___ roster(self):
        all_student_names    # list
        ___ grade_number __ s..(self.db.keys()):
            all_student_names.extend(self.db[grade_number])
        r.. all_student_names

    ___ grade(self, grade_number):
        r.. self.db[grade_number]
