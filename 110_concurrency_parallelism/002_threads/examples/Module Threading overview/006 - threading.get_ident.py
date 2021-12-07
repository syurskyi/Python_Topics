import threading, time, logging

def worker():
    name = threading.current_thread().name
    # использование 'threading.get_ident()'
    ident = threading.get_ident()
    # тоже самое можно получить через атрибут
    ident = threading.ident
    logging.debug(f'Starting {name}, id: {ident}')
    time.sleep(1)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)

for _ in range(3):
    thread = threading.Thread(target=worker)
    thread.start()

# [DEBUG] Starting Thread-1, id: 140190611068672
# [DEBUG] Starting Thread-2, id: 140190602675968
# [DEBUG] Starting Thread-3, id: 140190594283264