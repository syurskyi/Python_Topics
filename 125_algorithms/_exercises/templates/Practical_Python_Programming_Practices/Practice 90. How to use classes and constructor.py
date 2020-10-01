c_ company:
    ___  -(, employee_firstname, employee_surname):
        firstname _ employee_firstname
        surname _ employee_surname

    ___ employee
        r_ firstname + ' ' + surname

staff _   # list
___ i __ ra..(3):
    name _ i..("Insert firstname and surname: ")
    name _ name.sp..()
    staff.ap..(company(name[0], name[1]))

___ i __ staff:
    print(i.employee