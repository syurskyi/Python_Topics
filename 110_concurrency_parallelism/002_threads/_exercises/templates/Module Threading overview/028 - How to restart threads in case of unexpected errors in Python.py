import threading, time


def sensor_a():
    while True:
        time.sleep(1)
        print("Читаем показания датчика А")


def sensor_b():
    i = 0
    while True:
        time.sleep(1)
        if i == 1:
            # имитируем падение датчика
            raise KeyboardInterrupt
        print("Читаем показания датчика Б")
        i += 1


def threadwrap(threadfunc):
    def wrapper():
        while True:
            try:
                threadfunc()
            except BaseException as e:
                th_name = threading.current_thread().name
                print(f'Падение потока датчика {th_name}, перезапуск...')

    return wrapper


# словарь потоков
thread_dict = {
    'SENSOR_A': threading.Thread(target=sensor_a, name='SENSOR_A'),
    'SENSOR_B': threading.Thread(target=sensor_b, name='SENSOR_B')
}

# создаем потоки
threads = [t for t in thread_dict.values()]

# запускаем потоки
for t in threads:
    t.start()

# Читаем показания датчика Б
# Читаем показания датчика А
# Падение потока датчика SENSOR_B, перезапуск...
# Читаем показания датчика А
# Читаем показания датчика А
# Читаем показания датчика Б
# Читаем показания датчика А
# ...