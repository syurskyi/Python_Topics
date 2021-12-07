import threading, time


def worker():
    time.sleep(1)


for _ in range(6):
    thread = threading.Thread(target=worker)
    thread.start()

# использование 'threading.active_count()'
# 7 потоков = 6 порожденных + 1 основной
n_thread = threading.active_count()
print(n_thread)
# 7