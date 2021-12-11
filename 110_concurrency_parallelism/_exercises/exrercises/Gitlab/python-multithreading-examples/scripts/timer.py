# #!/usr/bin/python
#
#
# ## A Timer starts its work after a delay,
# ## and can be canceled at any point within that delay t__ period.
#
#
# ______ _
# ______ t__
# ______ l__
#
#
# l__.?
# 	?_l__.D..
#     ?_ _threadName -10_  _ m.. _
#
#
#
# ___ delayed
#     l__.d..('Thread program still running')
#     r_
#
# ___ Main
# 	t1  _.? 3 ?
# 	?.s..('Timer 1')
# 	t2  _.? 3 ?
# 	?.s..('Timer 2')
#
# 	l__.d..('Starting thread timers')
# 	?.s..
# 	?.s..
#
# 	l__.d..('We are waiting before canceling @' ?.g..
# 	t__.s.. 2
# 	l__.d.. 'Now canceling @' ?.g..
# 	?.c..
#
#
# __ ____ __ ______
# 	?