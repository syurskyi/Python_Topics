from ISP.Book.IBook import IBook


class ReferenceBook(IBook):

	def __init__(self):
		self.check_out_duration_in_days = -1
		self.pages = -1

	@property
	def library_id(self) -> str:
		return self.libraryId

	@library_id.setter
	def library_id(self, libraryId: str):
		self.libraryId = libraryId

	@property
	def title(self) -> str:
		return self.title

	@title.setter
	def title(self, titleName: str):
		self.titleName = titleName

	@property
	def author(self) -> str:
		return self.authorName

	@author.setter
	def author(self, authorName: str):
		self.authorName = authorName

	@property
	def pages(self) -> int:
		return self.num_pages

	@pages.setter
	def pages(self, num_pages: int):
		self.num_pages = num_pages
