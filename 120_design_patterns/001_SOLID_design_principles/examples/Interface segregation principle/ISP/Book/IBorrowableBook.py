from ISP.Book.IBook import IBook
from ISP.GeneralInterface.IBorrowable import IBorrowable


class IBorrowableBook(IBorrowable, IBook):
	raise NotImplementedError
