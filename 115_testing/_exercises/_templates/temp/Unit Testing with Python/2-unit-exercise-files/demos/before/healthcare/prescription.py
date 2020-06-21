____ d_t_ ______ date, timedelta

c_ Prescription:
    
    ___  -   name, dispense_date, days_supply
        name _ name
        dispense_date _ dispense_date
        days_supply _ days_supply
        
    ___ days_taken
        all_days _ [dispense_date + timedelta(days_i) ___ i __ ra..(days_supply)]
        r_ [day ___ day __ all_days __ day < date.today()]
