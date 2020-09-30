___ encode(message, rails
    r_ ''.join(_make_rails(message, rails))

___ decode(encoded_message, rails
    message = [None ___ _ __ range(le.(encoded_message))]
    ___ i, e __ enumerate(_make_rails(range(le.(encoded_message)), rails)):
        message[e] = encoded_message[i]
    r_ ''.join(message)

___ _make_rails(items, rails
    rail_lists = [[] ___ _ __ range(rails)]
    step, rail = 1, 0
    ___ char __ items:
        rail_lists[rail].append(char)
        __ not (0 <= rail + step < rails
            step *= -1
        rail += step
    r_ tu..(item ___ sublist __ rail_lists ___ item __ sublist)
