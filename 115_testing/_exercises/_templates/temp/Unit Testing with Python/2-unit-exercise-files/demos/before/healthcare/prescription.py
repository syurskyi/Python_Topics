____ datetime ______ date, timedelta

c_ Prescription:
    
    ___  -   name, dispense_date, days_supply
        name _ name
        dispense_date _ dispense_date
        days_supply _ days_supply
        
    ___ days_taken
        all_days _ [dispense_date + timedelta(days_i) for i in range(days_supply)]
        r_ [day for day in all_days if day < date.today()]
