_____ _, t__, logging

___ worker(
    # использование 'threading.current_thread()'
    # получаем экземпляр Thread и атрибутом
    # .name извлекаем имя потока
    thread_name = _.current_thread().name
    logging.debug(f'Starting {thread_name}')
    t__.s..(1)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)

th1 = _.?(t.. worker)
th1.start()
th2 = _.?(n.. 'worker', t.. worker)
th2.start()

# [DEBUG] Starting Thread-1
# [DEBUG] Starting worker