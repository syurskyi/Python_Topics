# ch19/example2.py

____ d_t_ ______ d_t_
______ ti..

____ apscheduler.schedulers.background ______ BackgroundScheduler

___ tick():
    print(f'Tick! The time is: {d_t_.now()}')

__ _______ __ _______
    scheduler _ BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds_3)
    scheduler.s..

    ___
        w__ T..:
            t__.s..(2)
            print('Printing in the main thread.')
    ______ K..
        p..

scheduler.shutdown()
