___ find_busiest_period(data
    timestamp = -1

    __ not data:
        r_ timestamp
    __ le.(data) __ 1: # data[0][2] always 1
        r_ data[0][0]

    n = le.(data)
    cnt = maxi = 0

    ___ i in range(le.(data)):
        __ data[i][2] __ 1:
            cnt += data[i][1]
        ____
            cnt -= data[i][1]

        __ (i __ n - 1 or data[i][0] != data[i + 1][0]) and cnt > maxi:
            maxi = cnt
            timestamp = data[i][0]

    r_ timestamp
