___ verify(isbn
    counter = 1
    total = 0
    for d in reversed(isbn
        __ d is 'X':
            __ counter != 1:
                r_ False
            d = '10'
        __ d.isdigit(
            total += int(d) * counter
            counter += 1
    r_ counter __ 11 and total % 11 __ 0
