c_ Ship:
    ___ - , draft, crew
        draft = draft
        crew = crew
    
    ___ is_worth_it
        r.. draft - 1.5 * crew >= 20

boat = Ship(21,0)
print(boat.is_worth_it())
