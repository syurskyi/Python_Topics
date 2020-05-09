____ datetime ______ date, timedelta

____ patient ______ Patient
____ prescription ______ Prescription

___ days_ago(days
    r_ date.today() - timedelta(days_days)

c_ TestPatient:
    
    ___ test_clash_with_no_prescriptions
        patient _ Patient(prescriptions_[])
        assert patient.clash([]) == set()
        
    ___ test_clash_with_one_irrelevant_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2)])
        assert patient.clash(["Prozac"]) == set()
        
    ___ test_clash_with_one_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2)])
        assert patient.clash(["Codeine"]) == {days_ago(days_2), days_ago(days_1)}

    ___ test_clash_with_two_different_prescriptions
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2),
                                         Prescription("Prozac",     dispense_date _ days_ago(days_2), days_supply_2)])
        assert patient.clash(["Codeine", "Prozac"]) == {days_ago(days_2), days_ago(days_1)}

    ___ test_clash_with_two_prescriptions_for_same_medication
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2),
                                         Prescription("Codeine", dispense_date _ days_ago(days_3), days_supply_2)])
        assert patient.clash(["Codeine"]) == {days_ago(days_3), days_ago(days_2), days_ago(days_1)}

    ___ test_days_taking_for_irrelevant_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2)])
        assert patient.days_taking("Prozac") == set()

    ___ test_days_taking
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2),
                                         Prescription("Codeine", dispense_date _ days_ago(days_3), days_supply_2)])
        assert patient.days_taking("Codeine") == {days_ago(days_3),
                                                     days_ago(days_2),
                                                     days_ago(days_1)}
  
    ___ test_clash_overlapping_today
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_3),
                                         Prescription("Prozac",     dispense_date _ days_ago(days_2), days_supply_3)])
        assert patient.clash(["Codeine", "Prozac"]) == {days_ago(days_2), days_ago(days_1)}
        