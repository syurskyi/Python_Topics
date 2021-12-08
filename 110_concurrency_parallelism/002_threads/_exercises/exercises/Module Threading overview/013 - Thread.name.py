import threading, time

def worker():
    # получаем экземпляр Thread и атрибутом
    # .name извлекаем имя потока
    thread_name = threading.current_thread().name
    print(f'Старт {thread_name}')
    time.sleep(1)

th1 = threading.Thread(target=worker)
# присвоение имени потока через атрибут
th1.name = 'FirstWorker'
th1.start()
# присвоение имени потока в конструкторе
th2 = threading.Thread(name='SecondWorker', target=worker)
th2.start()

# Старт FirstWorker
# Старт SecondWorker