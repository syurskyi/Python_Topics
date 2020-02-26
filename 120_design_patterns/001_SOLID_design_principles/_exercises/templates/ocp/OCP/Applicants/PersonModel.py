from OCP.Applicants.IApplicantModel import IApplicantModel
from OCP.Accounts.Accounts import Accounts


class PersonModel(IApplicantModel):

	def __init__(self):
		self.accounts = Accounts()

	@property
	def first_name(self):
		return self.firstName

	@first_name.setter
	def first_name(self, first_name):
		self.firstName = first_name

	@property
	def last_name(self):
		return self.lastName

	@last_name.setter
	def last_name(self, last_name):
		self.lastName = last_name
