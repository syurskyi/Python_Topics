_____ _, t__

___ worker(
    # получаем экземпляр Thread и атрибутом
    # .name извлекаем имя потока
    thread_name = _.current_thread().name
    print(f'Старт {thread_name}')
    t__.s..(1)

th1 = _.?(t.. worker)
# присвоение имени потока через атрибут
th1.name = 'FirstWorker'
th1.start()
# присвоение имени потока в конструкторе
th2 = _.?(n.. 'SecondWorker', t.. worker)
th2.start()

# Старт FirstWorker
# Старт SecondWorker