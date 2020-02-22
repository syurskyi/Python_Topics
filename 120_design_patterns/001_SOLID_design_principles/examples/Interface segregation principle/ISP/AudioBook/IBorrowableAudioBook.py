from ISP.AudioBook.IAudioBook import IAudioBook
from ISP.GeneralInterface.IBorrowable import IBorrowable


class IBorrowableAudioBook(IBorrowable, IAudioBook):
	raise NotImplementedError
