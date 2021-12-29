class Allergies(object):

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

    ___ __init__(self, score):
        self.score = score

    ___ is_allergic_to(self, allergy):
        r.. self.score & 1 << self._allergies.index(allergy)

    @property
    ___ lst(self):
        r.. [allergy ___ allergy __ self._allergies
                __ self.is_allergic_to(allergy)]
