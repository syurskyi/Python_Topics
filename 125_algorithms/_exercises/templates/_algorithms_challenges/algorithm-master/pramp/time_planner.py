___ meeting_planner(slots1, slots2, duration
    __ not slots1 or not slots2 or not duration:
        r_ []

    m, n = le.(slots1), le.(slots2)
    i = j = 0

    w___ i < m and j < n:
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])

        __ start + duration <= end:
            r_ [start, start + duration]

        __ slots1[i][1] < slots2[j][1]:
            i += 1
        ____
            j += 1

    r_ []
