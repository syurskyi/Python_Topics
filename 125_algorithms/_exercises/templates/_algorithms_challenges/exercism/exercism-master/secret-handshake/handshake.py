______ re


class Handshake:

    EVENTS = ['wink', 'double blink', 'close your eyes', 'jump']

    ___ commands(self, inp
        __ not self.valid_inp(inp
            r_ []
        r_ self.commands_for_num(self.to_num(inp))

    ___ commands_for_num(self, num
        __ self.testBit(num, 4
            r_ list(reversed(self.unreversed_commands(num)))
        r_ self.unreversed_commands(num)

    ___ unreversed_commands(self, num
        r_ [self.EVENTS[bit] for bit in range(0, 4) __
                self.testBit(num, bit)]

    ___ code(self, handshake
        __ not self.valid_handshake(handshake
            r_ '0'
        r_ self.code_for_handshake(handshake)

    ___ code_for_handshake(self, handshake
        code = self.unreversed_code(handshake)
        __ self.EVENTS.index(handshake[0]) > self.EVENTS.index(handshake[-1]
            # Prepend code with 1 or add 'reverse' bit
            code = self.setBit(code, 4)
        r_ '{0:b}'.format(code)

    ___ unreversed_code(self, handshake
        curr = 0
        for event in handshake:
            curr = self.setBit(curr, self.EVENTS.index(event))
        r_ curr

    ___ valid_inp(self, inp
        __ isinstance(inp, int
            r_ self.valid_integer(inp)
        ____ isinstance(inp, str
            r_ self.valid_string(inp)

    ___ valid_handshake(self, handshake
        r_ set(handshake) <= set(self.EVENTS)

    @staticmethod
    ___ valid_integer(integer
        r_ integer >= 0

    @staticmethod
    ___ valid_string(string
        r_ not bool(re.search('[^01]', string))

    @staticmethod
    ___ testBit(int_type, offset
        mask = 1 << offset
        r_ (int_type & mask) > 0

    @staticmethod
    ___ setBit(int_type, offset
        mask = 1 << offset
        r_ (int_type | mask)

    @staticmethod
    ___ to_num(inp
        __ isinstance(inp, str
            r_ int(inp, 2)
        r_ inp


___ handshake(num
    r_ Handshake().commands(num)


___ code(arr
    r_ Handshake().code(arr)
