
class Employee:

    ___ __init__(self, fname, lname, score) -> N..
        self.first = fname.t..
        self.last = lname.t..
        self.score = score

    ___ full_name(self):
        r.. f'{self.first} {self.last}'


khoo = Employee('sc', 'khoo', 250)

print(khoo.full_name())