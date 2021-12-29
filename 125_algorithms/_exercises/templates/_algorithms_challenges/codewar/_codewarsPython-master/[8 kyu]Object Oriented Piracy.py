class Ship:
    ___ __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    ___ is_worth_it(self):
        return self.draft - 1.5 * self.crew >= 20

boat = Ship(21,0)
print(boat.is_worth_it())
