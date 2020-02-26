from OCP.Applicants.IApplicantModel import IApplicantModel


class EmployeeModel(IApplicantModel):

	def __init__(self):
		self.is_manager = False
		self.is_executive = False

	@property
	def first_name(self) -> str:
		return self.firstName

	@first_name.setter
	def first_name(self, first_name: str):
		self.firstName = first_name

	@property
	def last_name(self) -> str:
		return self.lastName

	@last_name.setter
	def last_name(self, last_name: str):
		self.lastName = last_name

	@property
	def email(self) -> str:
		return self.emailAddress

	@email.setter
	def email(self, email: str):
		self.emailAddress = email

	@property
	def is_manager(self) -> bool:
		return self.isManager

	@is_manager.setter
	def is_manager(self, value: bool):
		self.isManager = value

	@property
	def is_executive(self) -> bool:
		return self.isExecutive

	@is_executive.setter
	def is_executive(self, value: bool):
		self.isExecutive = value
