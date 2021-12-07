_____ _, t__, logging

___ worker(
    name = _.current_thread().n..
    # использование 'threading.get_ident()'
    ident = _.get_ident()
    # тоже самое можно получить через атрибут
    ident = _.ident
    logging.debug(f'Starting {name}, id: {ident}')
    t__.s..(1)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
)

___ _ __ r..(3
    thread = _.?(t.. worker)
    thread.start()

# [DEBUG] Starting Thread-1, id: 140190611068672
# [DEBUG] Starting Thread-2, id: 140190602675968
# [DEBUG] Starting Thread-3, id: 140190594283264