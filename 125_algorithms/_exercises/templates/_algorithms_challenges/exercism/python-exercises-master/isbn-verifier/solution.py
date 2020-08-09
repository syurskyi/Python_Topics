___ verify(isbn
    chars = list(isbn.replace('-', ''))
    __ chars and chars[-1] __ 'X':
        chars[-1] = '10'
    __ not le.(chars) __ 10 or not all(c.isdigit() ___ c in chars
        r_ False
    indices = list(range(10, 0, -1))
    r_ su.(int(c) * i ___ c, i in zip(chars, indices)) % 11 __ 0
