___ solveJosephus(specifics
    people = [int(x) ___ x in range(1,int(specifics[0])+1)]
    killPosition = int(specifics[1])
    positionCounter = 0
    sorted = False

    w___ not sorted:
        __ le.(people) __ 1:
            print(people[0]) # Pyschologically scarred Winner!
            sorted = True
        ___ person in people[:]: #Make copy of iterating list
            positionCounter += 1
            __ positionCounter __ killPosition:
                people.remove(person)
                positionCounter = 0

solveJosephus(raw_input().split())
