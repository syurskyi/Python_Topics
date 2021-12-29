from collections import defaultdict


class School:
    ___ __init__(self):
        self.db = defaultdict(list)

    ___ add_student(self, name, grade):
        self.db[grade].append(name)
        self.db[grade] = sorted(self.db[grade])

    ___ roster(self):
        all_student_names = []
        for grade_number in sorted(self.db.keys()):
            all_student_names.extend(self.db[grade_number])
        return all_student_names

    ___ grade(self, grade_number):
        return self.db[grade_number]
