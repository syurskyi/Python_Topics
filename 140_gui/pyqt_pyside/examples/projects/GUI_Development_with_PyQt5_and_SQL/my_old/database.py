from PyQt5 import QtSql
from PyQt5.QtSql import *
from datetime import datetime

class Database:
    is_instance = False
    
    def __init__(self):
        # pass
        if not Database.is_instance:
            print('Database has been instantiated')
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('database.db')
            self.db.open()
            Database.is_instance = True
            print('Its still working')
        else:
            print('Has already been created')

    def get_salary_log_for_employee(self, id):
        query = QSqlQuery()

        queryString = """SELECT employee.first_name as "First Name", employee.last_name as "Last Name",
                          employee.department_name as "Department name", log_salary.salary as "Salary",
                          log_salary.reason as "Reason", log_salary.date as "Date"
                          FROM employee, log_salary
                          WHERE employee.id = log_salary.employee_id AND employee.id = :id"""
        query.prepare(queryString)
        query.bindValue(":id", id)
        query.exec()

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sublist = []

            for i in range(column_number):
                sublist.append(query.value(i))

            result_list.append(sublist)

        return (header_list, result_list)

    def get_position_log_for_employee(self, id):
        query = QSqlQuery()
        query_string = """SELECT employee.first_name as "First Name", employee.last_name as "Last Name",
                          employee.department_name as "Department name", log_position.position as "Position",
                          log_position.date as "Date"
                          FROM employee, log_position
                          WHERE employee.id = log_position.employee_id AND employee.id = :id"""
        query.prepare(query_string)
        query.bindValue(":id", id)
        query.exec()

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sublist = []

            for i in range(column_number):
                sublist.append(query.value(i))

            result_list.append(sublist)

        return (header_list, result_list)


    def get_employee_full_info(self, conditionList):
        print('I am in get_employee_full_info function ')
        query = QSqlQuery()

        query_string = """SELECT employee.id as ID, employee.first_name as "First Name", employee.last_name as "Last Name",
	                      employee.birthday as "Birthday", employee.department_name as "Department Name",
	                      log_salary.salary as "Salary", log_position.position as "Position"
                          FROM employee, log_salary, log_position
                          WHERE employee.id = log_salary.employee_id AND employee.id = log_position.employee_id
                          and log_salary.date = (SELECT max(date) FROM log_salary WHERE employee_id = employee.id)
                          and log_position.date = (SELECT max(date) FROM log_position WHERE employee_id = employee.id)"""

        condition = ""
        list_length = len(conditionList)

        for i in range(list_length - 1):
            condition += conditionList[i][0]
            condition += " = "
            condition += conditionList[i][1]
            condition += "and "

        if list_length > 0:
            condition += conditionList[list_length - 1][0]
            condition += " = "
            condition += conditionList[list_length -1][1]

        if condition:
            query_string += " and " + condition

        print(query_string)

        res = query.exec(query_string)

        record = query.record()
        column_number = record.count()

        header_list = []

        for i in range(column_number):
            header_list.append(record.field(i).name())

        result_list = []

        while query.next():
            sublist = []

            for i in range(column_number):
                sublist.append(query.value(i))

            result_list.append(sublist)

        return(header_list, result_list)


    def insert_new_salary(self, id, new_salary, reason):
        query = QSqlQuery()

        query.prepare("""INSERT INTO log_salary(employee_id, salary, date, reason)
                         VALUES(:e_id, :salary, :date, :reason)""")

        query.bindValue(":e_id", id)
        query.bindValue(":salary", new_salary)
        query.bindValue(":date", datetime.today().strftime('%Y-%m-%d'))
        query.bindValue(":reason", reason)

        return query.exec()

    def insert_new_position(self, id, new_position):
        query = QSqlQuery()

        query.prepare("""INSERT INTO log_position(employee_id, position, date)
                         VALUES(:e_id, :position, :date)""")

        query.bindValue(":e_id", id)
        query.bindValue(":position", new_position)
        query.bindValue(":date", datetime.today().strftime('%Y-%m-%d'))

        return query.exec()

    def get_last_employee_id(self):
        query= QSqlQuery()

        res = query.exec("""SELECT max(id) FROM employee""")

        if query.next():
            return query.value(0)

        return 0

    def insert_employee(self, employeeFullInfo):
        query = QSqlQuery()

        query.prepare("""INSERT INTO employee(first_name, last_name, birthday, department_name)
                         VALUES(:fn, :ln, :birthday, :department)""")

        query.bindValue(":fn", employeeFullInfo.firt_name)
        query.bindValue(":ln", employeeFullInfo.last_name)
        query.bindValue(":birhtday", employeeFullInfo.birthday)
        query.bindValue(":department", employeeFullInfo.department)

        query.exec()

        id = self.get_last_employee_id()

        query.prepare("""INSERT INTO log_position(employee_id, position, date)
                         VALUES(:e_id, :pos, :date)""")
        query.bindValue(":e_id", id)
        query.bindValue(":pos", employeeFullInfo.position)
        query.bindValue(":date", datetime.today().strftime('%Y-%m-%d'))

        query.exec()

        query.prepare("""INSERT INTO log_salary(employee_id, salary, date
                         VALUES(:e_id, :salary, :date)""")

        query.bindValue(":e_id", id)
        query.bindValue(":salary", employeeFullInfo.salary)
        query.bindValue(":date", datetime.today().strftime('%Y-%m-%d'))

        query.exec()

