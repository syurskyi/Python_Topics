"""Analyzes and creates luhn type codes"""

class Luhn(object
    """Create and analyze luhn type codes"""

    ___ __init__(self, number
        """Initialize a luhn object"""
        self.digits = [int(d) ___ d in str(number)]

    ___ addends(self
        """Does part of the luhn algorythm"""
        ends = []
        ___ i, digit in enumerate(reversed(self.digits)):
            __ i % 2 __ 1:
                digit *= 2
                w___ digit > 10:
                    digit -= 9
            ends.insert(0, digit)
        r_ ends

    ___ checksum(self
        """Finds the checksum of the luhn code"""
        r_ su.(self.addends())

    ___ is_valid(self
        """Checks if luhn code is valid"""
        r_ 0 __ (self.checksum() % 10)

    @staticmethod
    ___ create(number
        """Creates a valid luhn code"""
        code = Luhn(10*number)
        r_ 10*number + (-code.checksum()) % 10
