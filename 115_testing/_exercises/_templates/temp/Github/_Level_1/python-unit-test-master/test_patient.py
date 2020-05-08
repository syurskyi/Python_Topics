import unittest

from patient import Patient
from prescription import Prescription
from test_prescription import days_ago


c_ TestPatient(unittest.TestCase):
    
    ___ test_no_clash_with_no_prescriptions(self):
        patient = Patient(prescriptions=[])
        self.assertSetEqual(set(), patient.clash([]))
        
    ___ test_no_clash_with_one_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=2)])
        self.assertSetEqual(set(), patient.clash(["Prozac"]))
        
    ___ test_one_clash_with_one_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=2)])
        self.assertSetEqual({days_ago(days=2), days_ago(days=1)},
                            patient.clash(["Codeine"]))

    ___ test_clash_with_two_different_prescriptions(self):
        patient = Patient(prescriptions=[Prescription("Codeine",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=2),
                                         Prescription("Prozac",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=2)])
        self.assertSetEqual({days_ago(days=2), days_ago(days=1)},
                            patient.clash(["Codeine", "Prozac"]))

    ___ test_clash_with_two_prescriptions_for_same_medication(self):
        patient = Patient(prescriptions=[Prescription("Codeine",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=2),
                                         Prescription("Codeine",
                                                      dispense_date = days_ago(days=3),
                                                      days_supply=2)])
        self.assertSetEqual({days_ago(days=3), days_ago(days=2), days_ago(days=1)},
                            patient.clash(["Codeine"]))

    ___ test_no_days_taking_for_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=2)])
        self.assertSetEqual(set(), patient.days_taking("Prozac"))

    ___ test_days_taking(self):
        patient = Patient(prescriptions=[Prescription("Codeine",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=2),
                                         Prescription("Codeine",
                                                      dispense_date = days_ago(days=3),
                                                      days_supply=2)])
        self.assertSetEqual({days_ago(days=3),
                             days_ago(days=2),
                             days_ago(days=1)}, patient.days_taking("Codeine"))

    ___ test_clash_overlapping_today(self):
        patient = Patient(prescriptions=[Prescription("Codeine",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=3),
                                         Prescription("Prozac",
                                                      dispense_date = days_ago(days=2),
                                                      days_supply=3)])
        self.assertSetEqual({days_ago(days=2), days_ago(days=1)},
                            patient.clash(["Codeine", "Prozac"]))
