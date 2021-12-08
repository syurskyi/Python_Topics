import threading


def worker(i):
    """thread worker function"""
    print(f'Worker- {i}')


threads = []  # list
# запускаем функцию 'worker()'
# для выполнения в 5-ти потоках
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# блокируем дальнейшее выполнение программы
# пока не закончат выполняться все 5 потоков
[thread.join() for thread in threads]