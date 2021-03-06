from OCP.Applicants.EmployeeModel import EmployeeModel
from OCP.Accounts.IAccounts import IAccounts
from OCP.Applicants.IApplicantModel import IApplicantModel


class ManagerAccounts(IAccounts):

	@staticmethod
	def create(person: IApplicantModel):
		output = EmployeeModel()
		output.first_name = person.first_name
		output.last_name = person.last_name
		output.email = "{}{}@ocpcorp.com".format(output.first_name[:1], output.last_name)
		output.is_manager = True
		return output
