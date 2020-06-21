# ______ ti..
# ______ ra..
# ______ q..
#
# ____ t.. ______ T..  # still needed for daemon threads
# ____ c___.f.. ______ TPE..
#
# counter _ 0
# job_queue _ q__.Q..
# counter_queue _ q__.Q..
#
#
# ___ increment_manager
# 	g.. c..
# 	w__ T..
# 		increment _ c_q_.ge. # this waits until an item is available and locks the queue
# 		t__.s.. ra__.ra..
# 		old_counter _ c..
# 		t__.s.. ra__.ra..
# 		counter _ o.. + i..
# 		t__.s.. ra__.ra..
# 		j__.pu. _*New counter value |c..', '------------'))
# 		t__.s.. ra__.ra..
# 		c__.t_d..  # this unlocks the queue
#
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T.. target_i.. daemon_T.. .s..
#
#
#
# ___ printer_manager
# 	w__ T..
# 		___ line __ j__.ge.
# 			t__.s.. ra__.ra..
# 			print ?
# 		j__.t_d..
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T..(target_p.. d.._T.. .s..
#
#
# ___ increment_counter
# 	c__.pu. 1
# 	t__.s.. ra__.ra..
#
# w__ TPE.. max_workers_10 __ pool
# 	|?.s.. i.. ___ x __ ra.. 10
#
# c__.j..  # wait for counter_queue to be empty
# j__.j..  # wait for job_queue to be empty