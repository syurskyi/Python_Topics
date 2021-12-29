import re


class Handshake:

    EVENTS = ['wink', 'double blink', 'close your eyes', 'jump']

    ___ commands(self, inp):
        __ not self.valid_inp(inp):
            return []
        return self.commands_for_num(self.to_num(inp))

    ___ commands_for_num(self, num):
        __ self.testBit(num, 4):
            return list(reversed(self.unreversed_commands(num)))
        return self.unreversed_commands(num)

    ___ unreversed_commands(self, num):
        return [self.EVENTS[bit] for bit in range(0, 4) __
                self.testBit(num, bit)]

    ___ code(self, handshake):
        __ not self.valid_handshake(handshake):
            return '0'
        return self.code_for_handshake(handshake)

    ___ code_for_handshake(self, handshake):
        code = self.unreversed_code(handshake)
        __ self.EVENTS.index(handshake[0]) > self.EVENTS.index(handshake[-1]):
            # Prepend code with 1 or add 'reverse' bit
            code = self.setBit(code, 4)
        return '{0:b}'.format(code)

    ___ unreversed_code(self, handshake):
        curr = 0
        for event in handshake:
            curr = self.setBit(curr, self.EVENTS.index(event))
        return curr

    ___ valid_inp(self, inp):
        __ isinstance(inp, int):
            return self.valid_integer(inp)
        elif isinstance(inp, str):
            return self.valid_string(inp)

    ___ valid_handshake(self, handshake):
        return set(handshake) <= set(self.EVENTS)

    @staticmethod
    ___ valid_integer(integer):
        return integer >= 0

    @staticmethod
    ___ valid_string(string):
        return not bool(re.search('[^01]', string))

    @staticmethod
    ___ testBit(int_type, offset):
        mask = 1 << offset
        return (int_type & mask) > 0

    @staticmethod
    ___ setBit(int_type, offset):
        mask = 1 << offset
        return (int_type | mask)

    @staticmethod
    ___ to_num(inp):
        __ isinstance(inp, str):
            return int(inp, 2)
        return inp


___ handshake(num):
    return Handshake().commands(num)


___ code(arr):
    return Handshake().code(arr)
