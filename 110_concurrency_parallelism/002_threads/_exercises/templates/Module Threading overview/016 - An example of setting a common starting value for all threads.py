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
    print(f'{name_thread}: установка локального value')
    data.value = r__.randint(1, 100)
    show_value(data)


class MyLocal(_.local
    # !!! переопределяем конструктор класса
    ___ __init__(self, value
        super().__init__()
        self.value = value
        self.name = _.current_thread().name
        print(f'{self.name} стартовое значение {self.value}')


local_data = MyLocal(1000)
show_value(local_data)

___ i __ r..(2
    t = _.?(t.. worker, a.. (local_data,))
    t.start()

# MainThread стартовое значение 1000
# MainThread: value=1000
# Thread-1 стартовое значение 1000
# Thread-1: value=1000
# Thread-1: установка локального value
# Thread-1: value=31
# Thread-2 стартовое значение 1000
# Thread-2: value=1000
# Thread-2: установка локального value
# Thread-2: value=69