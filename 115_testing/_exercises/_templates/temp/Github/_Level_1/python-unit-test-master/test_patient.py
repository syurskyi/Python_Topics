______ u__

____ patient ______ Patient
____ prescription ______ Prescription
____ test_prescription ______ days_ago


c_ TestPatient?.?
    
    ___ test_no_clash_with_no_prescriptions
        patient _ Patient(prescriptions_[])
        assertSetEqual(se.(), patient.clash([]))
        
    ___ test_no_clash_with_one_irrelevant_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_2)])
        assertSetEqual(se.(), patient.clash(["Prozac"]))
        
    ___ test_one_clash_with_one_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_2)])
        assertSetEqual({days_ago(days_2), days_ago(days_1)},
                            patient.clash(["Codeine"]))

    ___ test_clash_with_two_different_prescriptions
        patient _ Patient(prescriptions_[Prescription("Codeine",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_2),
                                         Prescription("Prozac",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_2)])
        assertSetEqual({days_ago(days_2), days_ago(days_1)},
                            patient.clash(["Codeine", "Prozac"]))

    ___ test_clash_with_two_prescriptions_for_same_medication
        patient _ Patient(prescriptions_[Prescription("Codeine",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_2),
                                         Prescription("Codeine",
                                                      dispense_date _ days_ago(days_3),
                                                      days_supply_2)])
        assertSetEqual({days_ago(days_3), days_ago(days_2), days_ago(days_1)},
                            patient.clash(["Codeine"]))

    ___ test_no_days_taking_for_irrelevant_prescription
        patient _ Patient(prescriptions_[Prescription("Codeine",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_2)])
        assertSetEqual(se.(), patient.days_taking("Prozac"))

    ___ test_days_taking
        patient _ Patient(prescriptions_[Prescription("Codeine",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_2),
                                         Prescription("Codeine",
                                                      dispense_date _ days_ago(days_3),
                                                      days_supply_2)])
        assertSetEqual({days_ago(days_3),
                             days_ago(days_2),
                             days_ago(days_1)}, patient.days_taking("Codeine"))

    ___ test_clash_overlapping_today
        patient _ Patient(prescriptions_[Prescription("Codeine",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_3),
                                         Prescription("Prozac",
                                                      dispense_date _ days_ago(days_2),
                                                      days_supply_3)])
        assertSetEqual({days_ago(days_2), days_ago(days_1)},
                            patient.clash(["Codeine", "Prozac"]))
