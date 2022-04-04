_______ json
____ dateutil.tz _______ gettz
____ d__ _______ date, t.., tzinfo
____ dateutil.parser _______ p..
____ p.. _______ P..
_______ r__
____ t___ _______ Tuple, Optional, L..
_______ __

DATA_FILE_NAME = "test1.json"
TMP = P..(__.g..("TMP", "/tmp"


DATA_PATH = TMP / DATA_FILE_NAME
MY_TZ = gettz("America/New York")
UTC = gettz("UTC")


___ longest_streak(
    data_file: P.. = DATA_PATH, my_tz: Optional[tzinfo] = MY_TZ
) __ Optional[Tuple[date, date]]:
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
    w__ o.. data_file) __ f:
        data = json.l.. f)
    # You code from here
    commits = data 'commits'
    longest_streak = f__("-inf")
    start_date = end_date = N..
    
    day_timedelta = t..(d.._1)
    previous_date= current_start =N..
    current_streak = 1
    ___ i __ r..(l..(commits:
        commit = commits[i]
        __ commit 'passed' :
            date = p..(commit 'date' )
            date = date.astimezone(my_tz)


            date = date.date()


            __ date + day_timedelta __ previous_date:
                current_streak += 1
            ____:
                __ current_streak > longest_streak:
                    longest_streak = current_streak
                    start_date = current_start __ current_start ____ date
                    end_date = previous_date __ previous_date ____ date
                    

                current_streak = 1
                current_start = date


            previous_date = date


    
    __ current_streak > longest_streak:
        longest_streak = current_streak
        start_date = current_start
        end_date = previous_date

    
    
    __ start_date:

        r.. end_date,start_date






__ _______ __ _______
    streak = longest_streak()
    print(f"My longest streak went from {streak[0]} through {streak[1]}")
    print(f"The streak lasted {(streak[1]-streak[0]).days + 1} days")
