class Classroom:

    def __init__(self, code, max_num_students):
        self.code = code
        self.max_num_students = max_num_students
        # The list of students is initially empty
        self.students = {}

    def add_student(self, student):
        if len(self.students) < self.max_num_students:
            self.students[student.name] = student.grades

    def remove_student(self, student):
        del self.students[student.name]

    def __getitem__(self, student_name):
        return self.students[student_name]

class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

        

