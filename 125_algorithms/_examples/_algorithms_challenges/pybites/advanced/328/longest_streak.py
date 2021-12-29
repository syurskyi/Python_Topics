import json
from dateutil.tz import gettz
from datetime import date, timedelta, tzinfo
from dateutil.parser import parse
from pathlib import Path
import requests
from typing import Tuple, Optional, List
import os

DATA_FILE_NAME = "test1.json"
TMP = Path(os.getenv("TMP", "/tmp"))


DATA_PATH = TMP / DATA_FILE_NAME
MY_TZ = gettz("America/New York")
UTC = gettz("UTC")


def longest_streak(
    data_file: Path = DATA_PATH, my_tz: Optional[tzinfo] = MY_TZ
) -> Optional[Tuple[date, date]]:
    """Retrieve datetime strings of passed commits and calculate the longest
    streak from the user's data

    Note: The datetime strings will need to be used to create aware datetime objects

    All datetimes are in UTC, and the timezone of the user is part of the context
    for calculating a streak. Ex: 2019-10-14 01:58:48.129585+00:00 is 2019-10-13 in
    New York City. You will need to convert datetimes from UTC into the supplied timezone.

    The tests show an example of how a streak can change based on the timezone used.

    If the dataset has two or more streaks of the same length as longest, provide
    only the most recent streak.

    Return a tuple containing start and end date for the longest streak
    or None
    """
    with open(data_file) as f:
        data = json.load(f)
    # You code from here
    commits = data['commits']
    longest_streak = float("-inf")
    start_date = end_date = None
    
    day_timedelta = timedelta(days=1)
    previous_date= current_start =None
    current_streak = 1
    for i in range(len(commits)):
        commit = commits[i]
        if commit['passed']:
            date = parse(commit['date'])
            date = date.astimezone(my_tz)


            date = date.date()


            if date + day_timedelta == previous_date:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    start_date = current_start if current_start else date
                    end_date = previous_date if previous_date else date
                    

                current_streak = 1
                current_start = date


            previous_date = date


    
    if current_streak > longest_streak:
        longest_streak = current_streak
        start_date = current_start
        end_date = previous_date

    
    
    if start_date:

        return end_date,start_date 






if __name__ == "__main__":
    streak = longest_streak()
    print(f"My longest streak went from {streak[0]} through {streak[1]}")
    print(f"The streak lasted {(streak[1]-streak[0]).days + 1} days")
