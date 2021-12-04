_______ _______


counter = 0

lock = _______.Lock()

# lock.acquire()
# lock.release()


___ increment():
    global counter
    ___ i __ range(10**6):
        with lock:
            counter += 1
            # more locking
            # more locking

threads = []
___ i __ range(4):
    x = _______.T...(target=increment)
    threads.append(x)

___ t __ threads:
    t.start()

___ t __ threads:
    t.join()

print('Counter value:', counter)


# counter = x
# thread is locking
# thread <- counter = x
# thread -> counter = counter + 1 -> counter = x + 1
# release locking
# thread 2 is locking
# thread 2 <- counter = x + 1
# thread 2 -> counter = counter + 1 -> counter = x +1 + 1
# release locking

# counter = x + 2