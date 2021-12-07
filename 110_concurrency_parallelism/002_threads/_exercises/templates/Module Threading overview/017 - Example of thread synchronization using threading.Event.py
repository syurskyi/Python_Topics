_____ _, t__

___ wait_event(
    print('Старт WAIT_EVENT()')
    event.wait()
    print('Код обработки по событию в WAIT_EVENT()')

___ wait_timeout(time_out
    print('Старт WAIT_TIMEOUT() ')
    w__ n__ event.is_set(
        is_set = event.wait(timeout=time_out)
        print(f'TimeOut {time_out} секунды истек')
        __ is_set:
            print('Код обработки по событию в WAIT_TIMEOUT()')
        ____
            print('Пока ждем события, код обработки чего-то другого')
            t__.s..(3)

# установка глобального события
event = _.Event()

t1 = _.?(n.. 'blocking',
                  t.. wait_event)
t1.start()

t2 = _.?(n.. 'non-blocking',
                  t.. wait_timeout,
                  a.. (2,))
t2.start()

print('Ожидание перед вызовом Event.set()')
t__.s..(5)
event.set()
print('Установлено событие в основном потоке')


# Старт WAIT_EVENT()
# Старт WAIT_TIMEOUT()
# Ожидание перед вызовом Event.set()
# TimeOut 2 секунды истек
# Пока ждем события, код обработки чего-то другого
# Установлено событие в основном потоке
# Код обработки по событию в WAIT_EVENT()
# TimeOut 2 секунды истек
# Код обработки по событию в WAIT_TIMEOUT()