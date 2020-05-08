c_ Patient:

    ___  -   prescriptions=None):
        self.prescriptions = prescriptions or []

    ___ add_prescription  prescription):
        self.prescriptions.append(prescription)

    ___ days_taking  medicine_name):
        prescriptions = filter(lambda p: p.name == medicine_name, self.prescriptions)
        days = set()
        for prescription in prescriptions:
            days.update(prescription.days_taken())
        return days

    ___ clash  medicine_names):
        days_taking = [self.days_taking(medicine_name)
                       for medicine_name in medicine_names] \
                      or [set()]
        return set.intersection(*days_taking)
