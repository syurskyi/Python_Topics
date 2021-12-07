_____ _
rlock = _.RLock()
# первая блокировка
print('First try :', rlock.acquire())
# ('First try :', True)

# вторая блокировка
print('Second try:', rlock.acquire(timeout=0))
# ('Second try:', True)

# смотрим состояние - счетчик повторных блокировок count=2
print(rlock)
# <locked _thread.RLock object owner=140202475812672 count=2 at 0x7f83693acb10>

# разблокируем 2 раза
print(rlock.release())
print(rlock.release())
# смотрим состояние - счетчик повторных блокировок count=0
print(rlock)
# <locked _thread.RLock object owner=140202475812672 count=0 at 0x7f83693acb10>

# пробуем разблокировать уже разблокированное состояние
print(rlock.release())
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# RuntimeError: cannot release un-acquired lock