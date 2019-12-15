import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    results.append(result)


results = []

task1 = threading.Thread(
    target=handler,
    kwargs={'finished': 2 ** 12}
)
task2 = threading.Thread(
    target=handler,
    kwargs={'started': 2 ** 12, 'finished': 2 ** 24}
)  # 0 - 2^24

started_at = time.time()

task1.start()
task2.start()

task1.join()
task2.join()

print('RESULTS 1')
print('Time: {}'.format(time.time() - started_at))
print('Value: ', sum(results))

results = []
started_at = time.time()
handler(finished=2 ** 24)
print('RESULTS 2')
print('Time: {}'.format(time.time() - started_at))
print('Value: ', sum(results))
