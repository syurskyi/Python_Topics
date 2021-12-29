____ flux _______ XYZ, calculate_flux, identify_flux


___ test_calculate():
    calc = calculate_flux(XYZ)
    ... isi..(calc, l..)
    ... l..(calc) __ 11
    ... l..(calc[0]) __ 5

    *orig, dol, perc = calc[0]
    ... orig __ ["Cash", 120000, 115000]
    ... dol __ 5000
    ... round(perc, 2) __ 0.04


___ test_identify():
    flux = identify_flux(calculate_flux(XYZ))
    ... isi..(flux, l..)
    ... l..(flux) __ 5
    ... [act ___ act, *_ __ flux] __ [
        "Accounts Receivable",
        "Inventory",
        "Notes Receivable",
        "Accrued Payroll",
        "Retained Earnings",
    ]
