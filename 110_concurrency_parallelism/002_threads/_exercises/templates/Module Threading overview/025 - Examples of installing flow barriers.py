import threading, time


def worker(barrier):
    th_name = threading.current_thread().name
    print(f'{th_name} в ожидании барьера с {barrier.n_waiting} другими')
    worker_id = barrier.wait()
    print(f'{th_name} прохождение барьера {worker_id}')


# число потоков, при использовании
# барьеров оно должно быть постоянным
NUM_THREADS = 3

# установка барьера
barrier = threading.Barrier(NUM_THREADS)

threads = []
# создаем и запускаем потоки
for i in range(NUM_THREADS):
    th = threading.Thread(name=f'Worker-{i}',
                          target=worker,
                          args=(barrier,),
                          )
    threads.append(th)
    print(f'Запуск {th.name}')
    th.start()
    time.sleep(0.3)

# блокируем основной поток программы
# до завершения работы всех потоков
for thread in threads:
    thread.join()

# Запуск Worker-0
# Worker-0 в ожидании барьера с 0 другими
# Запуск Worker-1
# Worker-1 в ожидании барьера с 1 другими
# Запуск Worker-2
# Worker-2 в ожидании барьера с 2 другими
# Worker-2 прохождение барьера 2
# Worker-0 прохождение барьера 0
# Worker-1 прохождение барьера 1