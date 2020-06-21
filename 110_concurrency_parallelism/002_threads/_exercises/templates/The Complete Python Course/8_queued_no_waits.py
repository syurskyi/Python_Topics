# ______ t..
# ______ ra..
# ______ q..
#
# ____ t.. ______ T.. # still needed for daemon threads
# ____ c__.f.. ______ TPE..
#
# counter _ 0
# job_queue _ ?.Q..
# counter_queue _ ?.Q..
#
#
# ___ increment_manager
# 	g.. c..
# 	w__ T..
# 		increment _ c__.g..  # this waits until an item is available and locks the queue
# 		old_counter _ c..
# 		counter _ ? + i..
# 		j__.pu. _*New counter value |c..', '------------'))
# 		c__.t_d..  # this unlocks the queue
#
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T.. t.._? d.._T.. .s..
#
#
#
# ___ printer_manager
# 	w__ T..
# 		___ line __ j__.ge.
# 			print ?
# 		j__.t_d..
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T.. t.._? d.._T.. .s..
#
#
# ___ increment_counter
# 	c__.pu. 1
#
# w___ TPE.. m_w.._10 __ pool:
# 	|?.s.. ? ___ x __ ra.. 10
#
# c__.j..  # wait for counter_queue to be empty
# j__.j..  # wait for job_queue to be empty