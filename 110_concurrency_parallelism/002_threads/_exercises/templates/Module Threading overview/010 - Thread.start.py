_____ _, t__


___ worker(num_thread
    print(f'Старт потока №{num_thread}')
    t__.s..(1)
    print(f'Завершение работы потока №{num_thread}')


___ i __ r..(2
    # создаем экземпляры 'Thread' с функцией
    # 'worker()', которая запустится в отдельных
    # трех потоках. Позиционные аргументы для
    # функции 'worker()' передаются в кортеже `args`
    thread = _.?(t.. worker, a.. (i,))
    # запускаем экземпляр `thread`
    thread.start()

# Старт потока №0
# Старт потока №1
# Завершение работы потока №0
# Завершение работы потока №1