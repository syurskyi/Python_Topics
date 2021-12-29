_______ calendar
____ datetime _______ date
____ dateutil.relativedelta _______ relativedelta,FR,MO


ERROR_MSG = (
    "Unambiguous value passed, please specify either start_month or show_workdays"
)
FEDERAL_HOLIDAYS = (
    date(2020, 9, 7),
    date(2020, 10, 12),
    date(2020, 11, 11),
    date(2020, 11, 26),
    date(2020, 12, 25),
)
WFH = (calendar.TUESDAY, calendar.WEDNESDAY)
WEEKENDS = (calendar.SATURDAY, calendar.SUNDAY)
AT_HOME = WFH + WEEKENDS
HOURS = 8


___ four_day_weekends(*args,
        start_month: int = 8,
        paid_time_off: int = 200,
        year: int = 2020,
        show_workdays: bool = False
    ) -> N..
    """Generates four day weekend report

    The four day weekends are calculated from the start_month through the end of the year
    along with the number of work days for the same time period. The reports takes into
    account any holidays that might fall within that time period and days designated as
    working from home (WFH).

    If show_workdays is set to True, a report with the work days is generated instead of
    the four day weekend dates.

    Args:
        start_month (int, optional): Month to start. Defaults to 8.
        paid_time_off (int, optional): Paid vacation days
        year (int, optional): Year to calculate, defaults to current year
        show_workdays (bool, optional): Enables work day report. Defaults to False.

    Raises:
        ValueError: ERROR_MSG
    """


    __ args:
        raise ValueError(ERROR_MSG)
    ____:
        four_day_weekends = workdays =  0
        weekend_dates =[]
        workday_dates    # list
        current = date(year,start_month,1)
        current += relativedelta(weekday=FR)
        first_monday = current + relativedelta(weekday=MO(-1))
        __ first_monday.year __ year and first_monday.month __ start_month:
            workday_dates.a..(first_monday)
            



        while current.year __ year:
            monday = current + relativedelta(weekday=MO)
            thursday = current - relativedelta(days=1)
            __ thursday.year __ year  and thursday n.. __ FEDERAL_HOLIDAYS:
                workday_dates.a..(thursday)


            dates = [current,monday]
            __ monday.year __ year:
                __ a..(date n.. __ FEDERAL_HOLIDAYS ___ date __ dates):
                    weekend_dates.a..((current,monday))
                    four_day_weekends += 1
                ____:
                    __ monday n..  __ FEDERAL_HOLIDAYS:
                        workday_dates.a..(monday)
                    __ current n.. __ FEDERAL_HOLIDAYS:
                        workday_dates.a..(current)
            ____:
                __ current n.. __ FEDERAL_HOLIDAYS:
                    workday_dates.a..(current)






            current += relativedelta(weeks=1)
        


        last_thursday = current - relativedelta(days=1)
        __ last_thursday.year __ year and last_thursday n.. __ FEDERAL_HOLIDAYS:
            workday_dates.a..(last_thursday)
        workdays = l..(workday_dates)


        
        __ n.. show_workdays:
            length = l..(str(paid_time_off))
            number = 24 
            before_days = paid_time_off//8 
            new_balance = paid_time_off -  HOURS *  four_day_weekends * 2
            new_days = abs(new_balance // 8)
            title = f'{four_day_weekends} Four-Day Weekend{"s" __ four_day_weekends != 1 ____ ""}'
            print(f'{title:^{number}}')
            print('='* 24)

            labels = ['PTO:','BALANCE:']
            original = [paid_time_off,new_balance]
            new = [before_days,new_days]

            
            ___ label,value_1,value_2 __ zip(labels,original,new):
                print(f'{label:>8} {value_1:>{length}} ({value_2} days)')

            print()
            


            start_losing = (four_day_weekends * 2 - before_days)//2
            date_start_losing = N..
            __ start_losing > 0:
                date_start_losing = weekend_dates[start_losing]
            ___ i,(weekend_start,weekend_end) __ enumerate(weekend_dates):
                print(f"{weekend_start} - {weekend_end}",end='')
                __ (weekend_start,weekend_end) __ date_start_losing:
                    print(' *')
                ____:
                    print()


        ____:
            print(f'Remaining Work Days: {workdays * 8} ({workdays} days)')


            print('\n'.join(map(str,workday_dates)))




__ __name__ __ "__main__":
    four_day_weekends(start_month=10,show_workdays=True)
