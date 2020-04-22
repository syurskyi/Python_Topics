# ch19/example4.py
# Copied from: http://devcenter.heroku.com/articles/clock-processes-python

____ apscheduler.schedulers.blocking ______ BlockingScheduler

scheduler _ BlockingScheduler()

@scheduler.scheduled_job('interval', minutes_3)
___ timed_job():
    print('This job is run every three minutes.')

@scheduler.scheduled_job('cron', day_of_week_'mon-fri', hour_17)
___ scheduled_job():
    print('This job is run every weekday at 5pm.')

scheduler.s..
