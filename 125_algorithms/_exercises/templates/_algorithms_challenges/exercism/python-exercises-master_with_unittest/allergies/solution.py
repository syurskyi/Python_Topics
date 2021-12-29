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
        return self.score & 1 << self._allergies.index(allergy)

    @property
    ___ lst(self):
        return [allergy for allergy in self._allergies
                __ self.is_allergic_to(allergy)]
