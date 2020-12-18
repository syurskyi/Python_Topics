class Schnauzer:

    def __init__(self, name, age, color, blood_type, vaccines=None):
        self._name = name
        self._age = age
        self._color = color
        self._blood_type = blood_type
        self._vaccines = vaccines

    def schnauzer_introduction(self):
        print(f"Hi, my name is {self._name}. I'm a Schnauzer")
        
