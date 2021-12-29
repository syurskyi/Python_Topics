_______ re


class Handshake:

    EVENTS = ['wink', 'double blink', 'close your eyes', 'jump']

    ___ commands(self, inp):
        __ n.. self.valid_inp(inp):
            r.. []
        r.. self.commands_for_num(self.to_num(inp))

    ___ commands_for_num(self, num):
        __ self.testBit(num, 4):
            r.. l..(reversed(self.unreversed_commands(num)))
        r.. self.unreversed_commands(num)

    ___ unreversed_commands(self, num):
        r.. [self.EVENTS[bit] ___ bit __ r..(0, 4) __
                self.testBit(num, bit)]

    ___ code(self, handshake):
        __ n.. self.valid_handshake(handshake):
            r.. '0'
        r.. self.code_for_handshake(handshake)

    ___ code_for_handshake(self, handshake):
        code = self.unreversed_code(handshake)
        __ self.EVENTS.index(handshake[0]) > self.EVENTS.index(handshake[-1]):
            # Prepend code with 1 or add 'reverse' bit
            code = self.setBit(code, 4)
        r.. '{0:b}'.format(code)

    ___ unreversed_code(self, handshake):
        curr = 0
        ___ event __ handshake:
            curr = self.setBit(curr, self.EVENTS.index(event))
        r.. curr

    ___ valid_inp(self, inp):
        __ isi..(inp, int):
            r.. self.valid_integer(inp)
        ____ isi..(inp, str):
            r.. self.valid_string(inp)

    ___ valid_handshake(self, handshake):
        r.. set(handshake) <= set(self.EVENTS)

    @staticmethod
    ___ valid_integer(integer):
        r.. integer >= 0

    @staticmethod
    ___ valid_string(string):
        r.. n.. bool(re.search('[^01]', string))

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
        __ isi..(inp, str):
            r.. int(inp, 2)
        r.. inp


___ handshake(num):
    r.. Handshake().commands(num)


___ code(arr):
    r.. Handshake().code(arr)
