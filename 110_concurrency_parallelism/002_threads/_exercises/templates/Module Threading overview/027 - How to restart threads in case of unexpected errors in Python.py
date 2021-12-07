_____ _, t__

___ sensor_a(
    w__ T..:
        t__.s..(1)
        print("Читаем показания датчика А")

___ sensor_b(
    i = 0
    w__ T..:
        t__.s..(1)
        __ i == 1:
            # имитируем ошибку при чтении датчика
            raise KeyboardInterrupt
        print("Читаем показания датчика Б")
        i += 1

# словарь с потоки для чтения счетчиков
# словарь необходим для их перезапуска
thread_dict = {
'SENSOR_A': _.?(t.. sensor_a, n.. 'SENSOR_A'),
'SENSOR_B': _.?(t.. sensor_b, n.. 'SENSOR_B')
}

threads = [t ___ t __ thread_dict.values()]

# запускаем потоки
___ t __ threads:
    t.start()

# следим за потоками в реальном времени
w__ T..:
    # проходимся по объектам потоков
    ___ thread __ _.enumerate(
        # если поток умер
        __ n__ thread.isAlive(
            print(f'Поток, читающий {thread.n..} умер')
            # получаем из словаря `thread_dict`
            # поток по имени для его перезапуска
            restart = thread_dict[thread.n..]
            # пытаемся перезапустить
            restart.start()

# Читаем показания датчика А
# Читаем показания датчика Б
# Читаем показания датчика А
# Exception in thread sensor_b:
# Traceback (most recent call last):
# ...
# KeyboardInterrupt
# Поток, читающий SENSOR_B умер
# Перезапуск потока SENSOR_B
# Traceback (most recent call last):
# ...
# RuntimeError: threads can only be started once
# Читаем показания датчика А
# Читаем показания датчика А
# ...