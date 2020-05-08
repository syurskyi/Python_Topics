from datetime import date, timedelta

from patient import Patient
from prescription import Prescription

___ days_ago(days):
    return date.today() - timedelta(days=days)

c_ TestPatient:
    
    ___ test_clash_with_no_prescriptions(self):
        patient = Patient(prescriptions=[])
        assert patient.clash([]) == set()
        
    ___ test_clash_with_one_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=2)])
        assert patient.clash(["Prozac"]) == set()
        
    ___ test_clash_with_one_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=2)])
        assert patient.clash(["Codeine"]) == {days_ago(days=2), days_ago(days=1)}

    ___ test_clash_with_two_different_prescriptions(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=2),
                                         Prescription("Prozac",     dispense_date = days_ago(days=2), days_supply=2)])
        assert patient.clash(["Codeine", "Prozac"]) == {days_ago(days=2), days_ago(days=1)}

    ___ test_clash_with_two_prescriptions_for_same_medication(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=2),
                                         Prescription("Codeine", dispense_date = days_ago(days=3), days_supply=2)])
        assert patient.clash(["Codeine"]) == {days_ago(days=3), days_ago(days=2), days_ago(days=1)}

    ___ test_days_taking_for_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=2)])
        assert patient.days_taking("Prozac") == set()

    ___ test_days_taking(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=2),
                                         Prescription("Codeine", dispense_date = days_ago(days=3), days_supply=2)])
        assert patient.days_taking("Codeine") == {days_ago(days=3),
                                                     days_ago(days=2), 
                                                     days_ago(days=1)}
  
    ___ test_clash_overlapping_today(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date = days_ago(days=2), days_supply=3),
                                         Prescription("Prozac",     dispense_date = days_ago(days=2), days_supply=3)])
        assert patient.clash(["Codeine", "Prozac"]) == {days_ago(days=2), days_ago(days=1)}
        