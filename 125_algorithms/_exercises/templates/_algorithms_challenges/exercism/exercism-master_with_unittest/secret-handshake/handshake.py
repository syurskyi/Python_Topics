_______ __


c_ Handshake:

    EVENTS = ['wink', 'double blink', 'close your eyes', 'jump']

    ___ commands(self, inp):
        __ n.. valid_inp(inp):
            r.. []
        r.. commands_for_num(to_num(inp))

    ___ commands_for_num(self, num):
        __ testBit(num, 4):
            r.. l..(r..(unreversed_commands(num)))
        r.. unreversed_commands(num)

    ___ unreversed_commands(self, num):
        r.. [EVENTS[bit] ___ bit __ r..(0, 4) __
                testBit(num, bit)]

    ___ code(self, handshake):
        __ n.. valid_handshake(handshake):
            r.. '0'
        r.. code_for_handshake(handshake)

    ___ code_for_handshake(self, handshake):
        code = unreversed_code(handshake)
        __ EVENTS.index(handshake[0]) > EVENTS.index(handshake[-1]):
            # Prepend code with 1 or add 'reverse' bit
            code = setBit(code, 4)
        r.. '{0:b}'.f..(code)

    ___ unreversed_code(self, handshake):
        curr = 0
        ___ event __ handshake:
            curr = setBit(curr, EVENTS.index(event))
        r.. curr

    ___ valid_inp(self, inp):
        __ isi..(inp, int):
            r.. valid_integer(inp)
        ____ isi..(inp, s..):
            r.. valid_string(inp)

    ___ valid_handshake(self, handshake):
        r.. set(handshake) <= set(EVENTS)

    @staticmethod
    ___ valid_integer(integer):
        r.. integer >= 0

    @staticmethod
    ___ valid_string(string):
        r.. n.. bool(__.s..('[^01]', string))

    @staticmethod
    ___ testBit(int_type, offset):
        mask = 1 << offset
        r.. (int_type & mask) > 0

    @staticmethod
    ___ setBit(int_type, offset):
        mask = 1 << offset
        r.. (int_type | mask)

    @staticmethod
    ___ to_num(inp):
        __ isi..(inp, s..):
            r.. int(inp, 2)
        r.. inp


___ handshake(num):
    r.. Handshake().commands(num)


___ code(arr):
    r.. Handshake().code(arr)
