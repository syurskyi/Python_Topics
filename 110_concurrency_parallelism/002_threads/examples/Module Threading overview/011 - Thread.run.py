import threading, time


class Worker(threading.Thread):

    def __init__(self, num_thread):
        # вызываем конструктор базового класса
        super().__init__()
        # определяем аргументы собственного класса
        self.num_thread = num_thread

    def run(self):
        # теперь код функции 'worker()', которая должна
        # выполняться в отдельных потоках будет здесь
        print(f'Старт потока №{self.num_thread}')
        time.sleep(1)
        print(f'Завершение работы потока №{self.num_thread}')


for i in range(2):
    # Создаем экземпляры класса 'Worker()'
    th = Worker(i)
    # запускаем потоки
    th.start()

# Старт потока №0
# Старт потока №1
# Завершение работы потока №0
# Завершение работы потока №1