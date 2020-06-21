____ d_t_ ______ date, timedelta

____ prescription ______ Prescription

___ days_ago(days
    r_ date.today() - timedelta(days_days)

c_ TestPrescription:
    
    ___ test_days_taken_excludes_future_dates
        prescription _ Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_4)
        a.. prescription.days_taken() __ [days_ago(2), days_ago(1)]
