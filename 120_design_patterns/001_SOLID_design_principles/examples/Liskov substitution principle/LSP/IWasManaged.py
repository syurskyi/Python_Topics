from LSP.IEmployee import IEmployee
from LSP.IManager import IManager


class IManaged(IEmployee):

	@property
	def manager(self) -> IEmployee:
		raise NotImplementedError

	@manager.setter
	def manager(self, manager: IEmployee):
		raise NotImplementedError

	def assign_manager(self, manager: IEmployee):
		raise NotImplementedError
