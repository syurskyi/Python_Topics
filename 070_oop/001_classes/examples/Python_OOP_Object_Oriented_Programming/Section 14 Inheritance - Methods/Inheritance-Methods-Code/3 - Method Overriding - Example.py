class Teacher:

    def __init__(self, name, age, class_code):
        self.name = name
        self.age = age
        self.class_code = class_code

    def welcome_students(self):
        print("Welcome, dear students...")

class BiologyTeacher(Teacher):

    def welcome_students(self):
        # Call method from the superclass
        # Teacher.welcome_students(self)
        
        # Alternative Syntax
        super().welcome_students()

        # Expanded functionality
        print("Let's start our biology class")

class PhysicsTeacher(Teacher):

    def welcome_students(self):
        Teacher.welcome_students(self)
        print("Let's start our physics class")


