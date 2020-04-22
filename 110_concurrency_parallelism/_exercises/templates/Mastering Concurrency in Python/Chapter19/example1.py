# ch19/example1.py

____ datetime ______ datetime

____ apscheduler.schedulers.background ______ BlockingScheduler

___ tick():
    print(f'Tick! The time is: {datetime.now()}')

__ _______ __ _______
    scheduler _ BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds_3)

    ___
        scheduler.s..
        print('Printing in the main thread.')
    ______ K..
        p..

scheduler.shutdown()
