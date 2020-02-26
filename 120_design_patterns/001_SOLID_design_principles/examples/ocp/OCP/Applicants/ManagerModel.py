from OCP.Accounts.ManagerAccounts import ManagerAccounts
from OCP.Applicants.IApplicantModel import IApplicantModel

class ManagerModel(IApplicantModel):

	def __init__(self):
		self.accounts = ManagerAccounts()

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
