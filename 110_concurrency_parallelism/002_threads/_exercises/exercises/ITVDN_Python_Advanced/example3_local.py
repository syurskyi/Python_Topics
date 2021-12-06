import threading

print(threading.active_count())
current = threading.current_thread()
print(current.getName())
print(current.is_alive())
# # что произойдет, если попробуем еще раз его запустить
try:
    current.start()
except RuntimeError as e:
    print('ERROR: {error}'.format(error=e))
current.setName('SuperThread')
print(current.getName())
#
# # на самом деле setName, getName - это просто старый интерфейс.
# # В реальных задачах вы смело можете работаь напрямую с атрибутом name
current.name = 'SuperThread1'
print(current.name)
print(current.getName())
#
# # вывод всех запущенных и живых трэдов
print(threading.enumerate())
#
# # Напишем пример для демонстрации потокобезопасного хранилища данных.
thread_data = threading.local()
thread_data.value = 5


def print_results():
    print(threading.current_thread())
    print('Result: {}'.format(thread_data.value))


def counter(started, to_value):
    print(hasattr(thread_data, 'value')
    thread_data.value =
    ___ i __ ra.. ?
        t__.v.. +_ 1
    ?


task1 = ___.T.. t.._? a.._(0, 10), n.._'Task1'
task2 = ___.T.. t.._c.. a.._(100, 3), n.._'Task2')
?.n.. = *?
?.n.. = *?

?.s..
?.s..

p..

?.j..
?.j..
p..
