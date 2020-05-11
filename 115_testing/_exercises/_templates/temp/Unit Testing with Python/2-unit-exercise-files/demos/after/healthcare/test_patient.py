____ d_t_ ______ date, timedelta

____ patient ______ Patient
____ prescription ______ Prescription

___ days_ago(days
    r_ date.today() - timedelta(days_days)

c_ TestPatient:
    
    ___ test_clash_with_no_prescriptions
        patient _ Patient(prescriptions_[])
        a.. patient.clash([]) __ se.()
        
    ___ test_clash_with_one_irrelevant_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2)])
        a.. patient.clash(["Prozac"]) __ se.()
        
    ___ test_clash_with_one_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2)])
        a.. patient.clash(["Codeine"]) __ {days_ago(days_2), days_ago(days_1)}

    ___ test_clash_with_two_different_prescriptions
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2),
                                         Prescription("Prozac",     dispense_date _ days_ago(days_2), days_supply_2)])
        a.. patient.clash(["Codeine", "Prozac"]) __ {days_ago(days_2), days_ago(days_1)}

    ___ test_clash_with_two_prescriptions_for_same_medication
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2),
                                         Prescription("Codeine", dispense_date _ days_ago(days_3), days_supply_2)])
        a.. patient.clash(["Codeine"]) __ {days_ago(days_3), days_ago(days_2), days_ago(days_1)}

    ___ test_days_taking_for_irrelevant_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2)])
        a.. patient.days_taking("Prozac") __ se.()

    ___ test_days_taking
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_2),
                                         Prescription("Codeine", dispense_date _ days_ago(days_3), days_supply_2)])
        a.. patient.days_taking("Codeine") __ {days_ago(days_3),
                                                     days_ago(days_2),
                                                     days_ago(days_1)}
  
    ___ test_clash_overlapping_today
        patient _ Patient(prescriptions_[Prescription("Codeine", dispense_date _ days_ago(days_2), days_supply_3),
                                         Prescription("Prozac",     dispense_date _ days_ago(days_2), days_supply_3)])
        a.. patient.clash(["Codeine", "Prozac"]) __ {days_ago(days_2), days_ago(days_1)}
        