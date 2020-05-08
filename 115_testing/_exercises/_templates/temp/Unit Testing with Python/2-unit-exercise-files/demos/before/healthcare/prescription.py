from datetime import date, timedelta

c_ Prescription:
    
    ___  -   name, dispense_date, days_supply):
        self.name = name
        self.dispense_date = dispense_date
        self.days_supply = days_supply
        
    ___ days_taken(self):
        all_days = [self.dispense_date + timedelta(days=i) for i in range(self.days_supply)]
        return [day for day in all_days if day < date.today()]
