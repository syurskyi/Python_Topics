c_ Patient:

    ___  -   prescriptions_N..
        prescriptions _ prescriptions o. []

    ___ add_prescription  prescription
        prescriptions.append(prescription)

    ___ days_taking  medicine_name
        prescriptions _ filter(lambda p: p.name __ medicine_name, prescriptions)
        days _ set()
        for prescription in prescriptions:
            days.update(prescription.days_taken())
        r_ days

    ___ clash  medicine_names
        days_taking _ [days_taking(medicine_name)
                       for medicine_name in medicine_names] \
                      o. [set()]
        r_ set.intersection(*days_taking)
