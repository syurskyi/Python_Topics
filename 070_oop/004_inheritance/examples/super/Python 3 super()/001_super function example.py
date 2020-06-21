# At first, just look at the following code we used in our Python Inheritance tutorial. In that example code,
# the superclass was Person and the subclass was Student. So the code is shown below.

class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

        # defining class methods

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# # definition of subclass starts here

class Student(Person):
    studentId = ""

    def __init__(self, student_name, student_age, student_id):
        Person.__init__(self, student_name, student_age)
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # returns the value of student id


# # end of subclass definition
#
#
# # Create an object of the superclass
person1 = Person("Richard", 23)

# # call member methods of the objects
person1.show_age()

# # Create an object of the subclass
student1 = Student("Max", 22, "102")

print(student1.get_id())
student1.show_name()

# In the above example, we have called parent class function as:

# Person.__init__(self, student_name, student_age)
# We can replace this with python super function call as below.
#
#
# super().__init__(student_name, student_age)
# The output will remain the same in both the cases, as shown in the below image.

