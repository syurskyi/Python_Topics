from ISP.GeneralInterface.ILibraryItem import ILibraryItem


class IAudioBook(ILibraryItem):

	@property
	def run_time_in_minutes(self) -> int:
		raise NotImplementedError

	@run_time_in_minutes.setter
	def run_time_in_minutes(self, minutes: int):
		raise NotImplementedError
