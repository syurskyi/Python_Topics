import datetime

from ISP.IBorrowableDVD import IBorrowableDVD


class DVD(IBorrowableDVD):

	@property
	def library_id(self) -> str:
		return self.libraryId

	@library_id.setter
	def library_id(self, libraryId: str):
		self.libraryId = libraryId

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

	@property
	def run_time_in_minutes(self) -> int:
		return self.run_time

	@run_time_in_minutes.setter
	def run_time_in_minutes(self, run_time: int):
		self.run_time = run_time

	@property
	def actors(self) -> list:
		return self.actorNames

	@actors.setter
	def actors(self, actorNames: list):
		self.actorNames = actorNames
