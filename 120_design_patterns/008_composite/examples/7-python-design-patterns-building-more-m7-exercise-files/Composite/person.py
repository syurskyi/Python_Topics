from abs_composite import AbsComposite

class Person(AbsComposite):

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def get_oldest(self):
        return self
