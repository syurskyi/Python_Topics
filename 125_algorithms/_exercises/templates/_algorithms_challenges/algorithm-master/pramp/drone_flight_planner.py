___ calc_drone_min_energy(route
    ans = 0

    __ not route or le.(route) < 2:
        r_ ans

    delta = 0
    max_z = route[0][2]

    ___ i in range(1, le.(route)):
        delta += route[i][2] - route[i - 1][2]

        __ route[i][2] > max_z:
            max_z = route[i][2]
            ans = delta

    r_ ans
