class Student:
    
    def __init__(self, name, age, gps, id_):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.id = id_

    def __str__(self):
        return f"Student: {self.name}, age: {self.age}, gpa: {self.gpa}, id: {self.id}"
