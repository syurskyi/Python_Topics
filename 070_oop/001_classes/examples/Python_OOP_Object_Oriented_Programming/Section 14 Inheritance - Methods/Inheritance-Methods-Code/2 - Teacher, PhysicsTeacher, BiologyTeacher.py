class Teacher:

    def __init__(self, name, age, class_code):
        self.name = name
        self.age = age
        self.class_code = class_code

    def welcome_students(self):
        print("Welcome, dear students...")

class PhysicsTeacher(Teacher):

    def welcome(self):
        Teacher.welcome_students(self)
        print("Let's start our physics class")

class BiologyTeacher(Teacher):

    def welcome(self):
        Teacher.welcome_students(self)
        print("Let's start our biology class")
