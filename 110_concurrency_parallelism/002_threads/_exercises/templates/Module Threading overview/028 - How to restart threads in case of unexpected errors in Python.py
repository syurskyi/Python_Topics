_____ _, t__


___ sensor_a(
    w__ True:
        t__.s..(1)
        print("Читаем показания датчика А")


___ sensor_b(
    i = 0
    w__ True:
        t__.s..(1)
        __ i == 1:
            # имитируем падение датчика
            raise KeyboardInterrupt
        print("Читаем показания датчика Б")
        i += 1


___ threadwrap(threadfunc
    ___ wrapper(
        w__ True:
            try:
                threadfunc()
            except BaseException as e:
                th_name = _.current_thread().name
                print(f'Падение потока датчика {th_name}, перезапуск...')

    return wrapper


# словарь потоков
thread_dict = {
    'SENSOR_A': _.?(t.. sensor_a, n.. 'SENSOR_A'),
    'SENSOR_B': _.?(t.. sensor_b, n.. 'SENSOR_B')
}

# создаем потоки
threads = [t ___ t __ thread_dict.values()]

# запускаем потоки
___ t __ threads:
    t.start()

# Читаем показания датчика Б
# Читаем показания датчика А
# Падение потока датчика SENSOR_B, перезапуск...
# Читаем показания датчика А
# Читаем показания датчика А
# Читаем показания датчика Б
# Читаем показания датчика А
# ...