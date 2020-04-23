# ch19/example1.py

____ d_t_ ______ d_t_

____ apscheduler.schedulers.background ______ BlockingScheduler

___ tick():
    print(f'Tick! The time is: {d_t_.now()}')

__ _______ __ _______
    scheduler _ BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds_3)

    ___
        scheduler.s..
        print('Printing in the main thread.')
    ______ K..
        p..

scheduler.shutdown()
