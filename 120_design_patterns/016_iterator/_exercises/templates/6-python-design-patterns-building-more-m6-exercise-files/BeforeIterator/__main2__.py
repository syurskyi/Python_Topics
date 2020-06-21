from testdata import employees, departments

def main():

    print("Employees:")

    for i in range(1, employees.headcount+1):
        employee = employees.get_employee(i)
        print('Employee Id: {}; Name: {}; Date of Hire: {}'
              .format(employee.empid, employee.name, employee.hiredate)
             )

    print("Departments:")

    for i in range(*departments.departments_range):
        dept = departments.get_department(i)
        print('Department Id: {}; Name: {}; Date Established: {}'
              .format(dept.deptid, dept.name, dept.date_established)
             )

    print_summary(employees)
    print_summary(departments)

def print_summary(collection):
    pass
    # what goes here?
    # for what in what?

if __name__ == '__main__':
    main()
