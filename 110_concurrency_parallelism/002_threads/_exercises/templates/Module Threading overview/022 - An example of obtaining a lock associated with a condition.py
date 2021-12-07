import threading, time, queue

def consumer(cond, queue):
    """ждет определенного состояния для использования ресурсов"""
    th_name = threading.current_thread().name
    print(f'Запуск потока потребителя {th_name}')
    with cond:
        cond.wait()
        print(f'Обработка ресурса потребителем {th_name}')
        time.sleep(0.3)


def producer(cond, queue):
    """подготовка ресурса, для использования потребителями"""
    th_name = threading.current_thread().name
    print(f'Запуск потока производителя {th_name}')
    with cond:
        print(f'{th_name} готовит ресурс для потребителей')
        time.sleep(0.5)
        print(f'{th_name} ресурс ГОТОВ!')
        cond.notify_all()


# установка переменной условия
condition = threading.Condition()

# создание потоков потребителей
c1 = threading.Thread(name='Consumer-1',
                      target=consumer,
                      args=(condition,))
c2 = threading.Thread(name='Consumer-2',
                      target=consumer,
                      args=(condition,))
# создание потока потребителей производителя
p = threading.Thread(name='PRODUCER',
                     target=producer,
                     args=(condition,))
c1.start()
c2.start()
p.start()


# Запуск потока потребителя Consumer-1
# Запуск потока потребителя Consumer-2
# Запуск потока производителя PRODUCER
# PRODUCER готовит ресурс для потребителей
# PRODUCER ресурс ГОТОВ!
# Обработка ресурса потребителем Consumer-2
# Обработка ресурса потребителем Consumer-1