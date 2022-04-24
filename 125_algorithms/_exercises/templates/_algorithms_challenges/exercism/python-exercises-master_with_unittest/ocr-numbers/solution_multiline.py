____ t___ _______ L..

OCR_INPUT [
    ' _     _  _     _  _  _  _  _ ',
    '| |  | _| _||_||_ |_   ||_||_|',
    '|_|  ||_  _|  | _||_|  ||_| _|',
    '                              ',
]
OCR_WIDTH 3
OCR_HEIGHT 4


___ split_ocr_numbers(ocr_numbers: L..s.. __ L..[L..[s..]]:
    ocrs_split    # list
    len_line l..(ocr_numbers 0
    ___ start __ r..(0, len_line, OCR_WIDTH
        ocrs_split.a..(
            [line[start:start+OCR_WIDTH] ___ line __ ocr_numbers]
        )
    r.. ocrs_split

OCR_NUMBERS split_ocr_numbers(OCR_INPUT)


___ split_ocr_lines(ocr_numbers: L..s.. __ L..[L..[s..]]:
    ocr_lines    # list
    ___ start __ r..(0, l..(ocr_numbers), OCR_HEIGHT
        ocr_lines.a..(ocr_numbers[start:start+OCR_HEIGHT])
    r.. ocr_lines


___ validate_ocr_numbers(ocr_numbers: L..[s..]
    n_first_line l..(ocr_numbers 0
    __ n_first_line % OCR_WIDTH:
        message s..(n_first_line) + ' is not a multiple of ' + s..(OCR_WIDTH)
        r.. V...(message)
    __ l..(ocr_numbers) % OCR_HEIGHT:
        message 'numbers of rows is not a multiple of ' + s..(OCR_HEIGHT)
        r.. V...(message)
    __ a__(l..(line) !_ n_first_line ___ line __ ocr_numbers[1:]
        r.. V...('All lines must have the same length.')


___ validate_numbers(numbers: s..
    __ n.. numbers.i..
        r.. V... ? + ' is not a digit')


___ _convert_ocr_line(ocr_numbers: L..s.. __ s..
    ocrs_split split_ocr_numbers(ocr_numbers)
    numbers [
        s..(OCR_NUMBERS.i.. ocr __ ocr __ OCR_NUMBERS ____ '?'
        ___ ocr __ ocrs_split
    ]
    r.. ''.j.. ?)


___ number(ocr_numbers: L..s.. __ s..
    validate_ocr_numbers(ocr_numbers)
    r.. ','.j..(
        [_convert_ocr_line(line) ___ line __ split_ocr_lines(ocr_numbers)]
    )


___ grid(numbers: s..) __ L.. s..
    validate_numbers(numbers)
    ocr_numbers_split [
        OCR_NUMBERS[i..(number)] ___ number __ numbers
    ]
    r.. [
        ''.j..(lines) ___ lines __ z..(*ocr_numbers_split)
    ]


multiline_ocr [
                " _     _ ",
                " _|  ||_|",
                " _|  ||_|",
                "         ",
                " _     _ ",
                " _|  ||_|",
                " _|  ||_|",
                "         ",
]
... number(multiline_ocr) __ '318,318'


