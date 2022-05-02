_______ __


c_ Handshake:

    EVENTS =  'wink', 'double blink', 'close your eyes', 'jump' 

    ___ commands  inp
        __ n.. valid_inp(inp
            r..    # list
        r.. commands_for_num(to_num(inp

    ___ commands_for_num  num
        __ testBit(num, 4
            r.. l..(r..(unreversed_commands(num)))
        r.. unreversed_commands(num)

    ___ unreversed_commands  num
        r.. [EVENTS[bit] ___ bit __ r..(0, 4) __
                testBit(num, bit)]

    ___ code  handshake
        __ n.. valid_handshake(handshake
            r.. '0'
        r.. code_for_handshake(handshake)

    ___ code_for_handshake  handshake
        code unreversed_code(handshake)
        __ EVENTS.i.. handshake 0 > EVENTS.i.. handshake[-1]
            # Prepend code with 1 or add 'reverse' bit
            code setBit(code, 4)
        r.. '{0:b}'.f..(code)

    ___ unreversed_code  handshake
        curr 0
        ___ event __ handshake:
            curr setBit(curr, EVENTS.i.. event
        r.. curr

    ___ valid_inp  inp
        __ isi..(inp, i..
            r.. valid_integer(inp)
        ____ isi..(inp, s..
            r.. valid_string(inp)

    ___ valid_handshake  handshake
        r.. s..(handshake) <_ s..(EVENTS)

    $
    ___ valid_integer(integer
        r.. integer >_ 0

    $
    ___ valid_string(s__
        r.. n.. b..(__.s..('[^01]', s__

    $
    ___ testBit(int_type, offset
        mask 1 << offset
        r.. (int_type & mask) > 0

    $
    ___ setBit(int_type, offset
        mask 1 << offset
        r.. (int_type | mask)

    $
    ___ to_num(inp
        __ isi..(inp, s..
            r.. i..(inp, 2)
        r.. inp


___ handshake(num
    r.. Handshake().commands(num)


___ code(arr
    r.. Handshake().code(arr)
