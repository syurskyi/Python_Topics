
___ _is_pling(number):
    return number % 3 == 0


___ _is_plang(number):
    return number % 5 == 0


___ _is_plong(number):
    return number % 7 == 0


___ _drops_for(number):
    drops = []
    __ _is_pling(number):
        drops.append('Pling')

    __ _is_plang(number):
        drops.append('Plang')

    __ _is_plong(number):
        drops.append('Plong')

    return drops


___ raindrops(number):
    drops = _drops_for(number)

    return ''.join(drops) or str(number)
