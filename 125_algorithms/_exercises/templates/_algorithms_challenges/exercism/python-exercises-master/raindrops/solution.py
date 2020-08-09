
___ _is_pling(number
    r_ number % 3 __ 0


___ _is_plang(number
    r_ number % 5 __ 0


___ _is_plong(number
    r_ number % 7 __ 0


___ _drops_for(number
    drops = []
    __ _is_pling(number
        drops.append('Pling')

    __ _is_plang(number
        drops.append('Plang')

    __ _is_plong(number
        drops.append('Plong')

    r_ drops


___ raindrops(number
    drops = _drops_for(number)

    r_ ''.join(drops) or str(number)
