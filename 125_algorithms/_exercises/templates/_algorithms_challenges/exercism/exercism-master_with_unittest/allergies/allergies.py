class Allergies:

    ALLERGY_SCORES = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    ___ __init__(self, score):
        self.score = score
        self.lst = list(allergy for allergy in self.ALLERGY_SCORES __
                        self.is_allergic_to(allergy))

    ___ is_allergic_to(self, allergen):
        return self.ALLERGY_SCORES[allergen] & self.score
