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
            # имитируем ошибку при чтении датчика
            raise KeyboardInterrupt
        print("Читаем показания датчика Б")
        i += 1

# словарь с потоки для чтения счетчиков
# словарь необходим для их перезапуска
thread_dict = {
'SENSOR_A': threading.Thread(target=sensor_a, name='SENSOR_A'),
'SENSOR_B': threading.Thread(target=sensor_b, name='SENSOR_B')
}

threads = [t for t in thread_dict.values()]

# запускаем потоки
for t in threads:
    t.start()

# следим за потоками в реальном времени
while True:
    # проходимся по объектам потоков
    for thread in threading.enumerate():
        # если поток умер
        if not thread.isAlive():
            print(f'Поток, читающий {thread.name} умер')
            # получаем из словаря `thread_dict`
            # поток по имени для его перезапуска
            restart = thread_dict[thread.name]
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