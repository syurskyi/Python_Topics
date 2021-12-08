import threading, time, logging

def worker():
    # использование 'threading.current_thread()'
    # получаем экземпляр Thread и атрибутом
    # .name извлекаем имя потока
    thread_name = threading.current_thread().name
    logging.debug(f'Starting {thread_name}')
    time.sleep(1)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)


th1 = threading.Thread(target=worker)
th1.start()
th2 = threading.Thread(name='worker', target=worker)
th2.start()

# [DEBUG] Starting Thread-1
# [DEBUG] Starting worker