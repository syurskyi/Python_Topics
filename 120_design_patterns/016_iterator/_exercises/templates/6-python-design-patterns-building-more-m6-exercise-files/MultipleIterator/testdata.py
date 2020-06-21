from datetime import datetime
from employee import Employee
from employee_collection import Employees

TESTEMPLOYEES = (
    (1, 'Douglas Adams', datetime(1942, 7, 6)),
    (2, 'Sherlock Holmes', datetime(1887, 3, 15)),
    (3, 'Albert Einstein', datetime(1915, 11, 25)),
    (4, 'Sir John A Macdonald', datetime(1867, 8, 1)),
    (5, 'Theodore Roosevelt', datetime(1901, 9, 14))
)

employees = Employees()
for number, name, date in TESTEMPLOYEES:
    employees.add_employee(
        Employee(number, name, date)
    )
