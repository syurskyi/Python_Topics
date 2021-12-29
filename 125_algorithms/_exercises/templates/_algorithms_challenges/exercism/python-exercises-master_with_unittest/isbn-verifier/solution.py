___ verify(isbn):
    chars = l..(isbn.replace('-', ''))
    __ chars and chars[-1] __ 'X':
        chars[-1] = '10'
    __ n.. l..(chars) __ 10 o. n.. a..(c.isdigit() ___ c __ chars):
        r.. False
    indices = l..(r..(10, 0, -1))
    r.. s..(int(c) * i ___ c, i __ zip(chars, indices)) % 11 __ 0
