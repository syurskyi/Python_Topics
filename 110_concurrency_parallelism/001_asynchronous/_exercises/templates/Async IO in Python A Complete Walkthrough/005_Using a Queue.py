# #!/usr/bin/env python3
# # asyncq.py
#
# ______ a..
# ______ it.. __ it
# ______ __
# ______ ra..
# ______ ti..
#
# ? ___ makeitem size ? _ 5  s..
#     r_ __.ur.. ?.he.
#
# ? ___ randsleep a i.. _ 1 b i.. _ 5 caller_N..  N..
#     i _ ra__.r_i_ 0 10
#     __ caller
#         print _*|?| sleeping for |? seconds.
#     ? ?.sl.. ?
#
# ? ___ produce name in. q ?.Q..  N..
#     n _ ra__.r_i_ 0 10
#     ___ _ __ i_.re.. N.. ?  # Synchronous loop for each single producer
#         ? r_sl.. caller_f"Producer |n..
#         i _ ? m..
#         t _ t__.p_c..
#         ? q.pu. ? ?
#         print _*Producer |n..| added <|? > to queue.
#
# ? ___ consume name i.. q ?.Q.. N..
#     w__ T..
#         ? r_sl.. caller_f"Consumer |n..
#         i, t _ ? q.ge.
#         now _ t__.p_c..
#         print(_*Consumer |n.. got element <|? >"
#               _* in |no.-t;0.5_ seconds.")
#         q.t_d..
#
# ? ___ main nprod i.. ncon i..
#     q _ ?.Q..
#     producers _ ?.c_t.. p.. n, q|| ___ ? __ ra.. ?
#     consumers _ ?.c_t.. c.. n, q|| ___ ? __ ra.. ?
#     ? ?.g.. $p..
#     ? q.j..  # Implicitly awaits consumers, too
#     ___ c __ c..
#         ?.c..
#
# __ _________ __ ________
#     ______ arg...
#     ra__.se.. 444
#     parser _ a__.A..
#     ?.a_a.. "-p" "--nprod", t.._i.. d.._5
#     ?.a_a.. "-c" "--ncon", t.._i.. d.._10
#     ns _ p__.p_a..
#     start _ t__.p_c..
#     ?.ru. ? @@ns. -d
#     elapsed _ t__.p.._c.. - s..
#     print(_*Program completed in |?;0.5_ seconds.")