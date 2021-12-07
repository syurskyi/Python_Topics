import threading, time

def delayed():
    th_name = threading.current_thread().name
    print(f'Th:{th_name} Worker запущен')


# Создание и запуск потоков таймеров
t1 = threading.Timer(0.3, delayed)
t1.name = 'Timer-1'
t2 = threading.Timer(0.3, delayed)
t2.name = 'Timer-2'

print('Запуск таймеров')
t1.start()
t2.start()

print(f'Ожидание перед завершением {t2.name}')
time.sleep(0.2)
print(f'Завершение {t2.name}')
t2.cancel()
print('Выполнено')

# Запуск таймеров
# Ожидание перед завершением Timer-2
# Завершение Timer-2
# Выполнено
# Th:Timer-1 Worker запущен