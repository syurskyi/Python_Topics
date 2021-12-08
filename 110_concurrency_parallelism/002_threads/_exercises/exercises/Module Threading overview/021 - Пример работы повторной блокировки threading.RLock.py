# _____ _
# rlock = _.?
# # первая блокировка
# print('First try :', ?.a..
# # ('First try :', True)
#
# # вторая блокировка
# print 'Second try:', ?.a.. t.. 0
# # ('Second try:', True)
#
# # смотрим состояние - счетчик повторных блокировок count=2
# print ?
# # <locked _thread.RLock object owner=140202475812672 count=2 at 0x7f83693acb10>
#
# # разблокируем 2 раза
# print(?.r..
# print(?.r..
# # смотрим состояние - счетчик повторных блокировок count=0
# print(?)
# # <locked _thread.RLock object owner=140202475812672 count=0 at 0x7f83693acb10>
#
# # пробуем разблокировать уже разблокированное состояние
# print(?.r..
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # RuntimeError: cannot release un-acquired lock