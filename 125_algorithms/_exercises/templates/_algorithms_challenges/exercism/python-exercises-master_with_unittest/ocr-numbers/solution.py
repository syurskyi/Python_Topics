ROW 4
COL 3


___ split_ocr(ocr
    r.. [[ocr[i][COL * j:COL * (j + 1)] ___ i __ r..(ROW)]
            ___ j __ r..(l..(ocr[0]) // COL)]


ALL =  '    _  _     _  _  _  _  _  _ ',
       '  | _| _||_||_ |_   ||_||_|| |',
       '  ||_  _|  | _||_|  ||_| _||_|',
       '                              '

OCR_LIST split_ocr(ALL)
OCR_LIST [OCR_LIST[-1]] + OCR_LIST[:9]


___ number(ocr
    __ (l..(ocr) != ROW o. l..(ocr[0]) % COL o.
            any(l..(r) != l..(ocr[0]) ___ r __ ocr:
        r.. V...('Wrong grid size.')
    numbers split_ocr(ocr)
    d.. ''
    ___ n __ numbers:
        ___
            d.. += s..(OCR_LIST.i.. n
        ______ V..
            d.. += '?'
    r.. d..


___ grid(d..
    ___
        __ n.. d...i..
            r.. V...('String should be numeric.')
    ______ AttributeError:
        r.. V...('Argument should be a string.')
    ocr ['' ___ i __ r..(ROW)]
    ___ d __ d..:
        ___ r __ r..(ROW
            ocr[r] += OCR_LIST[i..(d)][r]
    r.. ocr
