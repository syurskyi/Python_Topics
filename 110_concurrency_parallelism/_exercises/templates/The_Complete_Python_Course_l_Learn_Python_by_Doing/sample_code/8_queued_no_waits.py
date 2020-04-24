# ______ t__
# ______ ra__
# ______ queue
#
# ____ ? ______ T..  # still needed for daemon threads
# ____ c__.f.. ______ TPE..
#
# counter _ 0
# job_queue _ q__.Q..
# counter_queue _ q__.Q..
#
#
# ___ increment_manager
# 	g.. counter
# 	w__ T..
# 		increment _ c__.g..  # this waits until an item is available and locks the queue
# 		old_counter _ c..
# 		counter _ o.. + i..
# 		j__.p.. _*New counter value |c.. ', '------------'))
# 		c__.t..  # this unlocks the queue
#
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T..(t.._ ? d..T.. .s..
#
#
#
# ___ printer_manager
# 	w__ T..
# 		___ line __ j__.g..
# 			print ?
# 		j__.t..
#
# # printer_manager and increment_manager run continuously because of the `daemon` flag.
# T.. t.._? d..T.. .s..
#
#
# ___ increment_counter
# 	c__.p.. 1
#
# w__ TPE.. m.._10 __ pool
# 	?.s.. ? ___ x __ ra.. 10
#
# c__.j..  # wait for c__ to be empty
# j_.j..  # wait for job_queue to be empty