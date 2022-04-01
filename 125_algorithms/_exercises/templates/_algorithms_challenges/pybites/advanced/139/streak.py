____ d__ _______ d__, t.., date
_______ __

TODAY = date(2018, 11, 12)


___ extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""

    data = data.s..

    
    dates = s..()
    lines = data.splitlines()
    ___ i,line __ e..(lines):
        __ i > 2 a.. i != l..(lines) - 1:
            date_ = __.s..(r'^\s*\|\s(\S+)\s\|',line).group(1)
            year,month,day = map(i..,date_.s..("-"))

            date_ = date y.._year, m.._month, d.._day)
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

    
    delta = t..(d.._1)
    day = TODAY - delta

    w.... day __ dates:
        streak += 1

        day -= delta

    

    __ TODAY __ dates:
        streak += 1

    r.. streak








