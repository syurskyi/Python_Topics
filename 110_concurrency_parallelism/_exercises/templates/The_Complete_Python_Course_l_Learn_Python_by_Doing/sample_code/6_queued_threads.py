# ____ ? ______ T..
# ______ t__
# ______ ra__
# ______ q..
#
# counter _ 0
# job_queue _ q__.Q..
# counter_queue _ q__.Q..
#
#
# ___ increment_manager
# 	g.. counter
# 	w__ T..
# 		increment _ c__.get  # this waits until an item is available and locks the queue
# 		t__.s.. ra__.ra__
# 		old_counter _ c..
# 		t__.s.. ra__.ra__
# 		counter _ o.. + i..
# 		t__.s.. ra__.ra__
# 		j__.p.. _*New counter value |c..', '------------'))
# 		t__.s.. ra__.ra__
# 		c__.t_d..  # this unlocks the queue
#
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T..(t.._? d..T.. .s..
#
#
#
# ___ printer_manager
# 	w__ T..
# 		___ line __ j__.g..
# 			t__.s.. ra__.ra__
# 			print ?
# 		j_q_.t_d..
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T.. t.._? d..T.. .s..
#
#
# ___ increment_counter
# 	c_q_.p.. 1
# 	t__.s.. ra__.ra__
#
#
# worker_threads _ T.. t.._? ___ thread __ ra.. 10
#
# ___ thread __ ?
# 	t__.s.. ra__.ra__
# 	?.s..
#
# ___ thread __ ?
# 	?.j..  # wait for it to finish
#
# c__.j..  # wait for counter_queue to be empty
# j__.j..  # wait for job_queue to be empty