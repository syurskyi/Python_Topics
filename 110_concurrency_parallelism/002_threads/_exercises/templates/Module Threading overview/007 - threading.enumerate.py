_____ _, t__, logging

___ worker(
    t__.s..(1)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)

___ _ __ r..(3
    thread = _.?(t.. worker)
    thread.start()

# использование 'threading.enumerate()'
# проходимся по экземплярам 'Thread'
# и из которых атрибутом '.name'
# извлекаем имена живых потоков
___ t __ _.enumerate(
    logging.debug(f'Thread Name: {t.name}')

# [DEBUG] Thread Name: MainThread
# [DEBUG] Thread Name: Thread-1
# [DEBUG] Thread Name: Thread-2
# [DEBUG] Thread Name: Thread-3