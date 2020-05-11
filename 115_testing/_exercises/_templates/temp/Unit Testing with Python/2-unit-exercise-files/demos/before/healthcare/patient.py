c_ Patient:
    
    ___  -   prescriptions_N..
        prescriptions _ prescriptions o. # list
    
    ___ add_prescription  prescription
        prescriptions.a..(prescription)
        
    ___ days_taking  medicine_name
        prescriptions _ filter(l___ p: p.name __ medicine_name, prescriptions)
        days _ set()
        ___ prescription __ prescriptions:
            days.u..(prescription.days_taken())
        r_ days
        
    ___ clash  medicine_names
        days_taking _ [days_taking(medicine_name) ___ medicine_name __ medicine_names] o. [set()]
        r_ set.intersection(*days_taking)
