c_ company:
    ___ - , employee_firstname, employee_surname):
        firstname  employee_firstname
        surname  employee_surname

    ___ employee
        r.. firstname + ' ' + surname

staff  []
___ i __ r..(3):
    name  input("Insert firstname and surname: ")
    name  name.s.. 
    staff.a..(company(name[0], name[1]))

___ i __ staff:
    print(i.employee())