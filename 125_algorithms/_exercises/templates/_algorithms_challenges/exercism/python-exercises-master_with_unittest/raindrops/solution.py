
___ _is_pling(number):
    r.. number % 3 __ 0


___ _is_plang(number):
    r.. number % 5 __ 0


___ _is_plong(number):
    r.. number % 7 __ 0


___ _drops_for(number):
    drops    # list
    __ _is_pling(number):
        drops.a..('Pling')

    __ _is_plang(number):
        drops.a..('Plang')

    __ _is_plong(number):
        drops.a..('Plong')

    r.. drops


___ raindrops(number):
    drops = _drops_for(number)

    r.. ''.j..(drops) o. s..(number)
