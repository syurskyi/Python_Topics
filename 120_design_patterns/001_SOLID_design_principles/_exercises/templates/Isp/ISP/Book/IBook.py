from ISP.ILibraryItem import ILibraryItem


class IBook(ILibraryItem):

	@property
	def pages(self) -> int:
		raise NotImplementedError

	@pages.setter
	def pages(self, num_pages: int):
		raise NotImplementedError

	@property
	def title(self) -> str:
		raise NotImplementedError

	@title.setter
	def title(self, titleName: str):
		raise NotImplementedError
