from OCP.Accounts.ExecutiveAccounts import ExecutiveAccounts
from OCP.Applicants.IApplicantModel import IApplicantModel


class ExecutiveModel(IApplicantModel):

	def __init__(self):
		self.accounts = ExecutiveAccounts()

	@property
	def first_name(self) -> str:
		return self.firstName

	@first_name.setter
	def first_name(self, firstName: str):
		self.firstName = firstName

	@property
	def last_name(self) -> str:
		return self.lastName

	@last_name.setter
	def last_name(self, lastName: str):
		self.lastName = lastName
