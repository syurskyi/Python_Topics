# Week Generator Solution
#
# Define the generator function week  which has a list of days.  Iterate over the days and yield each day.
# After "Sunday", the generator is exhausted.  It does not start over.


def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day
