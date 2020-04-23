# # ch14/example3.py
#
# ______ th..
# ______ ra..; ra__.se.. 0
# ______ ti..
#
# ___ update pause_period
#     g.. counter
#
#     w__ c_l..
#         current_counter _ ? # reading in shared resource
#         t__.s.. ? # simulating heavy calculations
#         counter _ c_c.. + 1 # updating shared resource
#
# pause_periods _ ra__.r_i. 0, 1 ___ i __ ra.. 20
#
# ###########################################################################
#
# counter _ 0
# count_lock _ ?.L..
#
# start _ t__.p_c..
# ___ i __ ra.. 20
#     ? p_p.. ?
#
# print('--Sequential version--')
# print _*Final counter: |c.. .')
# print _*Took |t__.p_c.. - s.. : .2_| seconds.')
#
# ###########################################################################
#
# counter _ 0
#
# threads _ ?.T.. t.._? a.._ p.._p.. i| || ___ ? __ ra.. 20
#
# start _ t__.p_c..
# ___ thread __ ?
#     ?.s..
# ___ ? __ ?
#     ?.j..
#
# print('--Concurrent version--')
# print _*Final counter: |c.. .')
# print _*Took |t__.p_c.. - s.. : .2_| seconds.')
#
# ###########################################################################
#
# print('Finished.')
