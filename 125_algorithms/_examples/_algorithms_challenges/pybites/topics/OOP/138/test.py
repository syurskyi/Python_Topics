
class Employee:

    def __init__(self, fname, lname, score) -> None:
        self.first = fname.title()
        self.last = lname.title()
        self.score = score

    def full_name(self):
        return f'{self.first} {self.last}'


khoo = Employee('sc', 'khoo', 250)

print(khoo.full_name())