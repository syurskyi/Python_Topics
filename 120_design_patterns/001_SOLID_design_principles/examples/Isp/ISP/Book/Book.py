import datetime

from ISP.IBorrowableBook import IBorrowableBook


class Book(IBorrowableBook):

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

	@property
	def check_out_duration_in_days(self) -> int:
		return self.check_out_duration_days

	@check_out_duration_in_days.setter
	def check_out_duration_in_days(self, num_days: int):
		self.check_out_duration_days = num_days

	@property
	def borrower(self) -> str:
		return self.borrowerName

	@borrower.setter
	def borrower(self, borrowerName: str):
		self.borrowerName = borrowerName

	@property
	def borrow_date(self) -> datetime.datetime:
		return self.borrowDate

	@borrow_date.setter
	def borrow_date(self, borrowDate: str):
		self.borrowDate = borrowDate

	def check_out(self, borrower: str):
		self.borrower = borrower
		self.borrowDate = datetime.datetime.now()

	def check_in(self):
		self.borrower = ""

	def get_due_date(self) -> datetime.datetime:
		final_date = self.borrowDate + datetime.timedelta(days=self.check_out_duration_in_days)
		return final_date
