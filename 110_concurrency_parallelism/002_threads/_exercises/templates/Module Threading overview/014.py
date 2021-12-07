_____ _


___ worker(i
    """thread worker function"""
    print(f'Worker-{i}')


threads = []
# запускаем функцию 'worker()'
# для выполнения в 5-ти потоках
___ i __ r..(5
    t = _.?(t.. worker, a.. (i,))
    threads.append(t)
    t.start()

# блокируем дальнейшее выполнение программы
# пока не закончат выполняться все 5 потоков
[thread.j.. ___ thread __ threads]