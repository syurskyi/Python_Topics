_____ _, t__, logging


___ worker(
    name = _.current_thread().n..
    t__.s..(1)
    logging.debug(f'Ending {name}')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)

# использование 'threading.main_thread()'
# получаем экземпляр основного потока
main_thread = _.main_thread()
# получаем имя основного потока
main_thread_name = main_thread.n..
logging.debug(f'{main_thread_name} starting...')

___ _ __ r..(3
    thread = _.?(t.. worker)
    thread.start()

___ t __ _.enumerate(
    # Список 'threading.enumerate()' включает в себя основной
    # поток и т.к. присоединение основного потока самого к себе
    # приводит к тупиковой ситуации, то его необходимо пропустить
    __ t is main_thread:
        continue
    thead_name = t.n..
    logging.debug(f'{main_thread_name} joining {thead_name}')
    t.j..

# [DEBUG] MainThread starting...
# [DEBUG] MainThread joining Thread-1
# [DEBUG] Ending Thread-1
# [DEBUG] MainThread joining Thread-2
# [DEBUG] Ending Thread-3
# [DEBUG] Ending Thread-2
# [DEBUG] MainThread joining Thread-3