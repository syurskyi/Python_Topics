from ISP.GeneralInterface.ILibraryItem import ILibraryItem


class IDVD(ILibraryItem):

	@property
	def actors(self) -> list:
		raise NotImplementedError

	@actors.setter
	def actors(self, actorNames: list):
		raise NotImplementedError

	@property
	def run_time_in_minutes(self) -> int:
		raise NotImplementedError

	@run_time_in_minutes.setter
	def run_time_in_minutes(self, run_time: int):
		raise NotImplementedError

	@property
	def title(self) -> str:
		raise NotImplementedError

	@title.setter
	def title(self, titleName: str):
		raise NotImplementedError
