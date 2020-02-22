class ILibraryItem:

	@property
	def author(self) -> str:
		raise NotImplementedError

	@author.setter
	def author(self, authorName: str):
		raise NotImplementedError

	@property
	def library_id(self) -> str:
		raise NotImplementedError

	@library_id.setter
	def library_id(self, libraryId: str):
		raise NotImplementedError
