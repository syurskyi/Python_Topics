#!python3
#list_timezones.py is a simple script to list all timezones and the associated current time.

______ pendulum
______ pytz

___ create_list(
    tz_list = []
    for tz in pytz.all_timezones:
        tz_list.append(tz)
    r_ tz_list

___ print_timezones(tz_list
    for tz in tz_list:
        print(tz + "  = {}".format(pendulum.now(tz).to_datetime_string()))

__ __name__ __ "__main__":
    print_timezones(create_list())