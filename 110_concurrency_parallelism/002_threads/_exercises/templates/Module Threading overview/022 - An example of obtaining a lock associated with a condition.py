_____ _, t__, q__

___ consumer(cond, q__
    """ждет определенного состояния для использования ресурсов"""
    th_name = _.c...n..
    print(f'Запуск потока потребителя {th_name}')
    w__ cond:
        cond.wait()
        print(f'Обработка ресурса потребителем {th_name}')
        t__.s..(0.3)


___ producer(cond, q__
    """подготовка ресурса, для использования потребителями"""
    th_name = _.c...n..
    print(f'Запуск потока производителя {th_name}')
    w__ cond:
        print(f'{th_name} готовит ресурс для потребителей')
        t__.s..(0.5)
        print(f'{th_name} ресурс ГОТОВ!')
        cond.notify_all()


# установка переменной условия
condition = _.Condition()

# создание потоков потребителей
c1 = _.?(n.. 'Consumer-1',
                      t.. consumer,
                      a.. (condition,))
c2 = _.?(n.. 'Consumer-2',
                      t.. consumer,
                      a.. (condition,))
# создание потока потребителей производителя
p = _.?(n.. 'PRODUCER',
                     t.. producer,
                     a.. (condition,))
c1.s..
c2.s..
p.s..


# Запуск потока потребителя Consumer-1
# Запуск потока потребителя Consumer-2
# Запуск потока производителя PRODUCER
# PRODUCER готовит ресурс для потребителей
# PRODUCER ресурс ГОТОВ!
# Обработка ресурса потребителем Consumer-2
# Обработка ресурса потребителем Consumer-1