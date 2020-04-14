# ____ t.. ______ T..
# ______ ti..
# ______ ra..
# ______ q..
#
# counter _ 0
# job_queue _ q__.Q..
# counter_queue _ q__.Q..
#
#
# ___ increment_manager
# 	g.. c..
# 	w___ T..
# 		increment _ c_q_.ge.  # this waits until an item is available and locks the queue
# 		t__.s.. ra__.ra..
# 		old_counter _ counter
# 		t__.s.. ra__.ra..
# 		counter _ o.. + i..
# 		t__.s.. ra__.ra..
# 		j__.pu. _*New counter value |c..', '------------'))
# 		t__.s.. ra__.ra..
# 		c__.t_d..  # this unlocks the queue
#
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T.. target_increment_manager daemon_T.. .s..
#
#
#
# ___ printer_manager
# 	w___ T..
# 		___ line __ j__.ge.
# 			t__.s.. ra__.ra..
# 			print ?
# 		j__.t_d..
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T.. (target_printer_manager daemon_T.. .s..
#
#
# ___ increment_counter
# 	c__.p.. 1
# 	t__.s.. ra__.ra..
#
#
# worker_threads _ |T.. target_increment_counter| ___ thread __ ra.. 10
#
# ___ thread __ ?
# 	t__.s..(ra__.ra..
# 	?.s..
#
# ___ thread __ ?
# 	?.j..  # wait for it to finish
#
# c_q_.j..  # wait for counter_queue to be empty
# j_q_.j..  # wait for job_queue to be empty