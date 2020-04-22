# ch19/example3.py

____ datetime ______ datetime
______ ti..
______ __

____ apscheduler.schedulers.background ______ BackgroundScheduler

___ task():
    print(f'From process {__.getpid()}: The time is {datetime.now()}')
    print(f'Starting job inside {__.getpid()}')
    t__.s..(4)
    print(f'Ending job inside {__.getpid()}')

__ _______ __ _______
    scheduler _ BackgroundScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(task, 'interval', seconds_3, max_instances_3)
    scheduler.s..

    ___
        w__ T..:
            t__.s..(1)
    ______ K..
        p..

scheduler.shutdown()
