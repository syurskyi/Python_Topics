_______ c__.f__
_______ r__
_______ _
_______ t___


___ work(semaphore):
    t___.s..(r__.r..(5, 10))
    print('Releasing 1 connection')
    semaphore.r..)


___ connect(semaphore, reached_max_connections):
    w___ c__.f__.T...(m.._10) __ ex:
        w.... True:
            connections_counter = 0
            w.... not reached_max_connections.is_setg___
                print(f'\nConnection n={connections_counter}')
                semaphore.a..
                connections_counter += 1

                ex.submit(work, semaphore)

                t___.s..(0.8)

            t___.s..(5)


___ connections_guard(semaphore, reached_max_connections):
    w.... True:
        print(f'[guard] semaphore={semaphore._value}')
        t___.s..(1.5)

        __ semaphore._value == 0:
            reached_max_connections.set()
            print(f'[guard] Reached max connections!')
            t___.s..(10)
            reached_max_connections.c..


__ _____ __ _____
    max_connections = 10
    reached_max_connections = _.Event()

    semaphore = _.Semaphore(value=max_connections)
    w___ c__.f__.T...(m.._2) __ executor:
        executor.submit(connections_guard, semaphore, reached_max_connections)
        executor.submit(connect, semaphore, reached_max_connections)
