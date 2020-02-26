from OCP.Applicants.ExecutiveModel import ExecutiveModel
from OCP.Applicants.PersonModel import PersonModel
from OCP.Applicants.ManagerModel import ManagerModel


if __name__ == '__main__':

	person1 = PersonModel()
	person2 = ManagerModel()
	person3 = ExecutiveModel()
	person4 = ManagerModel()

	person1.first_name = 'Harry'
	person1.last_name = 'Potter'

	person2.first_name = 'Hermoine'
	person2.last_name = 'Granger'

	person3.first_name = 'Ron'
	person3.last_name = 'Weisley'

	person4.first_name = 'Ron'
	person4.last_name = 'Weisley'

	applicants = [person1, person2, person3, person4]

	employees = list()

	for person in applicants:
		try:
			employees.append(person.accounts.create(person))
		except Exception as e:
			print(e)
			print(person)

	for emp in employees:
		try:
			print("{} {} : {} : IsManager {} : IsExecutive {}".format(emp.first_name, emp.last_name, emp.email, emp.is_manager, emp.is_executive))
		except Exception as e:
			print(e)
