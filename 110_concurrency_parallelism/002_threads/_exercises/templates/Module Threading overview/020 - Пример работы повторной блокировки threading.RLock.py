import threading
lock = threading.Lock()
print(lock)
# <unlocked _thread.lock object at 0x7f836cdb0b48>

# первая блокировка
print('First try :', lock.acquire())
# ('First try :', True)
print(lock)
# <locked _thread.lock object at 0x7f836cdb0b48>

# вторая блокировка
print('Second try:', lock.acquire(timeout=0))
# ('Second try:', False)