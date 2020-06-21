# ______ time
# ____ c__.f.. ______ TPE..
#
# ####### SINGLE THREAD
#
# ___ ask_user
# 	start _ t__.t__
# 	user_input _ in.. 'Enter your name: '
# 	greet _ _*Hello, |?
# 	print ?
# 	print('ask_user: ', t__.t__ - s..
#
# ___ complex_calculation
# 	print('Started calculating...')
# 	start _ t__.t__
# 	|x**2 ___ ? __ ra.. 20000000
# 	print('complex_calculation: ', t__.t__ - s..
#
#
# # With a single thread, we can do one at a t__—e.g.
# start _ t__.t__
# ?
# ?
# print('Single thread total t__: ', t__.t__ - s.. '\n\n')
#
#
# ####### TWO THREADS
#
#
# # With two threads, we can do them both at once...
# start _ t__.t__
#
# w___ TPE.. max_workers_2) __ pool
# 	?.s.. c..
# 	?.s.. a..
#
# # All this does is we don't have to call pool.shutdown()
#
# print('Two thread total t__: ', t__.t__ - s..
#
# # Run this and see what happens!
