_____ _, r__


___ show_value(data
    name_thread = _.current_thread().name
    try:
        val = data.value
    except AttributeError:
        print(f'{name_thread}: Нет локального значения value')
    else:
        print(f'{name_thread}: value={val}')


___ worker(data
    name_thread = _.current_thread().name
    show_value(data)
    print(f'Установка значения value для потока {name_thread}.')
    data.value = r__.randint(1, 100)
    show_value(data)


local_data = _.local()
show_value(local_data)
# установка значения value для
# основного потока программы
local_data.value = 1000
show_value(local_data)

___ i __ r..(2
    t = _.?(t.. worker, a.. (local_data,))
    t.start()

# MainThread: Нет локального значения value
# MainThread: value=1000
# Thread-1: Нет локального значения value
# Установка значения value для потока Thread-1.
# Thread-1: value=63
# Thread-2: Нет локального значения value
# Установка значения value для потока Thread-2.
# Thread-2: value=35