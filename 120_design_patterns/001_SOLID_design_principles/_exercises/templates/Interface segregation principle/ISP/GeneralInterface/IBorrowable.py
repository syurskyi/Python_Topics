import datetime


class IBorrowable:
	@property
	def borrow_date(self) -> datetime.datetime:
		raise NotImplementedError

	@borrow_date.setter
	def borrow_date(self, borrowDate: datetime.datetime):
		raise NotImplementedError

	@property
	def check_out_duration_in_days(self) -> int:
		raise NotImplementedError

	@check_out_duration_in_days.setter
	def check_out_duration_in_days(self, days: int):
		raise NotImplementedError

	def check_in(self):
		raise NotImplementedError

	def check_out(self, borrower: str):
		raise NotImplementedError

	def get_due_date(self) -> datetime.datetime:
		raise NotImplementedError
