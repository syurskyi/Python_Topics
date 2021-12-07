import threading, time, logging


def worker():
    name = threading.current_thread().name
    time.sleep(1)
    logging.debug(f'Ending {name}')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)

# использование 'threading.main_thread()'
# получаем экземпляр основного потока
main_thread = threading.main_thread()
# получаем имя основного потока
main_thread_name = main_thread.name
logging.debug(f'{main_thread_name} starting...')

for _ in range(3):
    thread = threading.Thread(target=worker)
    thread.start()

for t in threading.enumerate():
    # Список 'threading.enumerate()' включает в себя основной
    # поток и т.к. присоединение основного потока самого к себе
    # приводит к тупиковой ситуации, то его необходимо пропустить
    if t is main_thread:
        continue
    thead_name = t.name
    logging.debug(f'{main_thread_name} joining {thead_name}')
    t.join()

# [DEBUG] MainThread starting...
# [DEBUG] MainThread joining Thread-1
# [DEBUG] Ending Thread-1
# [DEBUG] MainThread joining Thread-2
# [DEBUG] Ending Thread-3
# [DEBUG] Ending Thread-2
# [DEBUG] MainThread joining Thread-3