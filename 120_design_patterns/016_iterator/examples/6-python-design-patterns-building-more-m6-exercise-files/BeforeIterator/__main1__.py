from testdata import employees

def main():

    print("Employees:")

    for i in range(1, employees.headcount+1):
        employee = employees.get_employee(i)
        print('Employee Id: {}; Name: {}; Date of Hire: {}'
              .format(employee.empid, employee.name, employee.hiredate)
             )

if __name__ == '__main__':
    main()
