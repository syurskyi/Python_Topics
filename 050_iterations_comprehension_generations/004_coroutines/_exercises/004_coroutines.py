# # -*- coding: utf-8 -*-
#
# # producer-consumer-coroutines
#
# # """
# # Сопрограмма (англ. coroutine) — компонент программы, обобщающий понятие
# # подпрограммы, который дополнительно поддерживает множество входных точек
# # (а не одну, как подпрограмма) и остановку и продолжение выполнения с
# # сохранением определённого положения.
#
# # Rolling our own Next method
#
# c_ Squares
#     ___ - ______
#         ____.i _ 0
#
#     __ next_ ___
#         result _ ____.i ** 2
#         ____.i +_ 1
#         r_ ?
#
# sq _ ?
# ?.n..
# ?.n..
#
# ___ i __ r... 10
#     print sq.n...
#
# # Coroutines
# # The word co actually comes from cooperative.
# # A coroutine is a generalization of subroutines (think functions), focused on cooperation between routines.
# # If you have some concepts of multi-threading, this is similar in some ways.
# # But whereas in multi-threaded applications the operating system usually decides when to suspend one thread and
# # resume another, without asking permission, so-called preemptive multitasking,
# # here we have routines that voluntarily yield control to something else - hence the term cooperative.
#
# # Coroutines
# #
# # We can specify a maximum size for the queue when create it - this allows us to limit the number of items in the queue.
# #
# # (Note that I'm avoiding calling it the start and end of the queue,
# # because what you consider the start/end of the queue might depend on how you are using it)
#
# f_ col__ ______ d...
#
# dq _ d... 1 2 3 4 5
# print ?
#
# ?.app.. 100
# print ?
#
# ?.app..l... -10
# print ?
#
# ?.po.
# print ?
# ?.po.l..
#
# # Coroutines
# # We can create a capped queue:
# # As you can see the first item (2) was automatically discarded from the left of the queue when we added 300 to the right.
# # We can also find the number of elements in the queue by using the len() function:
# # as well as query the maxlen:
#
# f_ col___ ______ d...
# dq _ d.. 1 2 3 4 ; m..l.._5
# ?.app.. 100
# print ?
# ?.app.. 200
# print ?
# ?.app.. 300
# print ?
#
# print le. ?
# ?.m..l..
#
# # Coroutines
# # Now let's create an empty queue, and write two functions - one that will add elements to the queue, and one that will consume elements from the queue:
#
# ___ produce_elements dq
#     ___ i __ r... 1 36
#         ?.app..l.. i
#
# ___ consume_elements dq
#     w____ le. d. > 0
#         item _ ?.po..
#         print processing item i..
#
# ___ coordinator(
#     dq _ d..
#     producer _ p..._e... d.
#     c.._el.. d.
#
# coo...
#
# # Coroutines
# # The goal is to process these after some time, and not wait until all the items have been added to the queue -
# # maybe the incoming stream is infinite even.
# # In that case, we want to "pause" adding elements to the queue, process (consume) those items,
# # then once they've all been processed we want to resume adding elements, and rinse and repeat.
# # We'll use a capped deque, and change our producer and consumers slightly, so that each one does it's work,
# # the yields control back to the caller once it's done with its work - the producer adding elements to the queue,
# # and the consumer removing and processing elements from the queue:
#
# ___ produce_elements dq n
#     ___ i __ r.. 1 n
#         ?.app..l.. ?
#         __ le. ? __ ?.m..l..
#             print queue full - yielding control
#             y....
#
#
# ___ consume_elements dq
#     w____ T..
#         w____ l.. ? > 0
#             print processing * ?.po.
#         print queue empty - yielding control
#         y....
#
#
# ___ coordinator
#     dq _ d... m..l.._10
#     producer _ p.._e.. dq 36
#     consumer _ c.._e.. dq
#     w____ T...
#         ...
#             print producing...
#             n____ pr..
#         ____ S.
#             # producer finished
#             ....
#         ....
#             print consuming...
#             n___ c...
#
#
# coordinator()
#
#
