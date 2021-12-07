import threading, time, logging

def worker():
    time.sleep(1)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)

for _ in range(3):
    thread = threading.Thread(target=worker)
    thread.start()

# использование 'threading.enumerate()'
# проходимся по экземплярам 'Thread'
# и из которых атрибутом '.name'
# извлекаем имена живых потоков
for t in threading.enumerate():
    logging.debug(f'Thread Name: {t.name}')

# [DEBUG] Thread Name: MainThread
# [DEBUG] Thread Name: Thread-1
# [DEBUG] Thread Name: Thread-2
# [DEBUG] Thread Name: Thread-3