class company:
    ___ __init__(self, employee_firstname, employee_surname):
        self.firstname = employee_firstname
        self.surname = employee_surname

    ___ employee(self):
        r_ self.firstname + ' ' + self.surname

staff =   # list
___ i __ range(3):
    name = input("Insert firstname and surname: ")
    name = name.split()
    staff.append(company(name[0], name[1]))

___ i __ staff:
    print(i.employee())