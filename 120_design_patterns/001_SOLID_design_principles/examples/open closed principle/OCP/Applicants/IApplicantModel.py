import abc


class IApplicantModel:

	@property
	@abc.abstractmethod
	def first_name(self) -> str:
		raise NotImplementedError()

	@first_name.setter
	@abc.abstractmethod
	def first_name(self, firstName: str):
		raise NotImplementedError

	@property
	@abc.abstractmethod
	def last_name(self) -> str:
		raise NotImplementedError

	@last_name.setter
	@abc.abstractmethod
	def last_name(self, lastName: str):
		raise NotImplementedError
