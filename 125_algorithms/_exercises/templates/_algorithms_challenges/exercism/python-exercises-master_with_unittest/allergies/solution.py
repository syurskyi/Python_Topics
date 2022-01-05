c_ Allergies(object):

    _allergies = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    ___ - , score):
        score = score

    ___ is_allergic_to  allergy):
        r.. score & 1 << _allergies.index(allergy)

    $
    ___ lst
        r.. [allergy ___ allergy __ _allergies
                __ is_allergic_to(allergy)]
