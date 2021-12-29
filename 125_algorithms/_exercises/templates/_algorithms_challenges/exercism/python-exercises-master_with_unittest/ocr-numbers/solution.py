ROW = 4
COL = 3


___ split_ocr(ocr):
    r.. [[ocr[i][COL * j:COL * (j + 1)] ___ i __ r..(ROW)]
            ___ j __ r..(l..(ocr[0]) // COL)]


ALL = ['    _  _     _  _  _  _  _  _ ',
       '  | _| _||_||_ |_   ||_||_|| |',
       '  ||_  _|  | _||_|  ||_| _||_|',
       '                              ']

OCR_LIST = split_ocr(ALL)
OCR_LIST = [OCR_LIST[-1]] + OCR_LIST[:9]


___ number(ocr):
    __ (l..(ocr) != ROW o. l..(ocr[0]) % COL o.
            any(l..(r) != l..(ocr[0]) ___ r __ ocr)):
        raise ValueError('Wrong grid size.')
    numbers = split_ocr(ocr)
    digits = ''
    ___ n __ numbers:
        try:
            digits += s..(OCR_LIST.index(n))
        except ValueError:
            digits += '?'
    r.. digits


___ grid(digits):
    try:
        __ n.. digits.isdigit():
            raise ValueError('String should be numeric.')
    except AttributeError:
        raise ValueError('Argument should be a string.')
    ocr = ['' ___ i __ r..(ROW)]
    ___ d __ digits:
        ___ r __ r..(ROW):
            ocr[r] += OCR_LIST[int(d)][r]
    r.. ocr
