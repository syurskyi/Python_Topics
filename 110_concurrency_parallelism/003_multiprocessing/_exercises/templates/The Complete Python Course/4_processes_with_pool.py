# ______ ti..
# ____ concurrent.futures ______ PPE..
#
# ####### SINGLE PROCESS
#
# ___ ask_user
# 	start _ t__.t__
# 	user_input _ i.. Enter your name:
# 	greet _ _*Hello, |?
# 	print ?
# 	print('ask_user: ', t__.t__ - s..
#
# ___ complex_calculation
# 	print('Started calculating...')
# 	start _ t__.t__
# 	x**2 ___ ? __ ra.. 20000000
# 	print('complex_calculation: ', t__.t__ - s..
#
#
# # With a single thread, we can do one at a time—e.g.
# start _ t__.t__
# a..
# c..
# print('Single thread total time: ' t__.t__ - s.. '\n\n')
#
#
# ####### TWO PROCESSES
#
#
# # With two processes, we can do them both at once...
# start _ t__.t__
#
# w__ PPE..(max_workers_2) __ pool
# 	p__.s.. c..
# 	p__.s.. c..
#
# print('Two process total time: ', t__.t__ - s..
#
# # Run this and see what happens!
#
