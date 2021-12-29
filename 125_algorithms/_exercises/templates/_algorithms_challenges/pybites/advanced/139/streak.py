____ datetime _______ datetime, timedelta, date
_______ re

TODAY = date(2018, 11, 12)


___ extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""

    data = data.strip()

    
    dates = set()
    lines = data.splitlines()
    ___ i,line __ enumerate(lines):
        __ i > 2 and i != l..(lines) - 1:
            date_ = re.search(r'^\s*\|\s(\S+)\s\|',line).group(1)
            year,month,day = map(int,date_.split("-"))

            date_ = date(year=year,month=month,day=day)
            dates.add(date_)

    r.. dates







___ calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    streak = 0

    
    delta = timedelta(days=1)
    day = TODAY - delta

    while day __ dates:
        streak += 1

        day -= delta

    

    __ TODAY __ dates:
        streak += 1

    r.. streak








