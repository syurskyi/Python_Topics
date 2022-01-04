___ verify(isbn):
    chars = l..(isbn.r..('-', ''))
    __ chars a.. chars[-1] __ 'X':
        chars[-1] = '10'
    __ n.. l..(chars) __ 10 o. n.. a..(c.isdigit() ___ c __ chars):
        r.. F..
    indices = l..(r..(10, 0, -1))
    r.. s..(i..(c) * i ___ c, i __ z..(chars, indices)) % 11 __ 0
