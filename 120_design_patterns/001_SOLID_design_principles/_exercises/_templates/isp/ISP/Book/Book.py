# ______ datetime
#
# ___ ISP.IBorrowableBook ______ IB..
#
#
# c_ Book IB..
#
# 	?p..
# 	___ library_id __ ?
# 		r_ lI..
#
# 	??.?
# 	___ library_id  libraryId ?
# 		self.libraryId = libraryId
#
# 	?p..
# 	___ title __ ?
# 		r_ ti..
#
# 	??.?
# 	___ title titleName ?
# 		??  ?
#
# 	?p..
# 	___ author __ ?
# 		r_ aN..
#
# 	??.?
# 	___ author authorName ?
# 		??  ?
#
# 	?p..
# 	___ pages __ ?
# 		r_ n_p..
#
# 	??.?
# 	___ pages num_pages ?
# 		??   ?
#
# 	?p..
# 	___ check_out_duration_in_days __ ?
# 		r_ check_out_duration_days
#
# 	??.?
# 	___ check_out_duration_in_days num_days: ?
# 		ch... _ n_d..
#
# 	?p..
# 	___ borrower __ ?
# 		r_ bN..
#
# 	??.?
# 	___ borrower borrowerName ?
# 		??  ?
#
# 	?p..
# 	___ borrow_date __ d_t_.d_t_
# 		r_ bD..
#
# 	??.?
# 	___ borrow_date borrowDate ?
# 		??  ?
#
# 	___ check_out borrower ?
# 		??  ?
# 		?bD.. _ d_t_.d_t_.n..
#
# 	___ check_in
# 		?bo.. = ""
#
# 	___ get_due_date __ d_t_.d_t_
# 		final_date _ bD.. + d_t_.ti..de.. days_?ch...
# 		r_ ?
