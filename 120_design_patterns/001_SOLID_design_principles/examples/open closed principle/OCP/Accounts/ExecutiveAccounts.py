from OCP.Accounts.IAccounts import IAccounts
from OCP.Applicants.IApplicantModel import IApplicantModel
from OCP.Applicants.EmployeeModel import EmployeeModel

class ExecutiveAccounts(IAccounts):

	@staticmethod
	def create(person: IApplicantModel) -> EmployeeModel:
		output = EmployeeModel()
		output.first_name = person.first_name
		output.last_name = person.last_name
		output.email = "{}.{}@ocpcorp.com".format(output.first_name, output.last_name)

		output.is_executive = True
		output.is_manager = True

		return output
