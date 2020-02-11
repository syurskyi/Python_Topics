
class Dog:
    
    def __init__(self, name, age, color, blood_type, vaccines=None):
        self.name = name
        self.age = age
        self.color = color
        self._blood_type = blood_type
        self.vaccines = vaccines
        

class Poodle(Dog):
    
    def poodle_introduction(self):
        print(f"Hi, my name is {self._name}. I'm a Poodle")


class Schnauzer(Dog):
    
    def schnauzer_introduction(self):
        print(f"Hi, my name is {self._name}. I'm a Schnauzer")



        


