from collections ______ defaultdict


class School:
    ___ __init__(self
        self.db = defaultdict(list)

    ___ add_student(self, name, grade
        self.db[grade].append(name)
        self.db[grade] = sorted(self.db[grade])

    ___ roster(self
        all_student_names = []
        ___ grade_number in sorted(self.db.keys()):
            all_student_names.extend(self.db[grade_number])
        r_ all_student_names

    ___ grade(self, grade_number
        r_ self.db[grade_number]
