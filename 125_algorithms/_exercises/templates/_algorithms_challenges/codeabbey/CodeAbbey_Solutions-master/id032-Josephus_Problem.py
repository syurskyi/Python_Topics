___ solveJosephus(specifics):
    people = [int(x) ___ x __ r..(1,int(specifics[0])+1)]
    killPosition = int(specifics[1])
    positionCounter = 0
    s.. = False

    while n.. s..:
        __ l..(people) __ 1:
            print(people[0]) # Pyschologically scarred Winner!
            s.. = True
        ___ person __ people[:]: #Make copy of iterating list
            positionCounter += 1
            __ positionCounter __ killPosition:
                people.remove(person)
                positionCounter = 0

solveJosephus(raw_input().split())
