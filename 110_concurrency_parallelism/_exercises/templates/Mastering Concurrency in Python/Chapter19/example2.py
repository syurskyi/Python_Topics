# ch19/example2.py

____ datetime ______ datetime
______ ti..

____ apscheduler.schedulers.background ______ BackgroundScheduler

___ tick():
    print(f'Tick! The time is: {datetime.now()}')

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
