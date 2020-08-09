___ encode(message, rails
    r_ ''.join(_make_rails(message, rails))

___ decode(encoded_message, rails
    message = [None for _ in range(le.(encoded_message))]
    for i, e in enumerate(_make_rails(range(le.(encoded_message)), rails)):
        message[e] = encoded_message[i]
    r_ ''.join(message)

___ _make_rails(items, rails
    rail_lists = [[] for _ in range(rails)]
    step, rail = 1, 0
    for char in items:
        rail_lists[rail].append(char)
        __ not (0 <= rail + step < rails
            step *= -1
        rail += step
    r_ tuple(item for sublist in rail_lists for item in sublist)
