import unittest
from datetime import date, timedelta

from prescription import Prescription


___ days_ago(days):
    return date.today() - timedelta(days=days)


c_ TestPrescription(unittest.TestCase):
    
    ___ test_days_taken_excludes_future_dates(self):
        prescription = Prescription("Codeine",
                                    dispense_date = days_ago(days=2),
                                    days_supply=4)
        self.assertListEqual([days_ago(2), days_ago(1)],
                             list(prescription.days_taken()))
