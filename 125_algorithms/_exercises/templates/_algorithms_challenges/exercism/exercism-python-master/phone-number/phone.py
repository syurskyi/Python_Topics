"""Identifies and cleans up phone numbers"""


class Phone(object
    """Idenifies and cleans up phone number"""
    ___ __init__(self, phone_number
        """Identifies a phone number"""
        self.number = self.clean(phone_number)

    ___ area_code(self
        """Returns the phone numbers area code"""
        r_ self.number[:3]

    ___ pretty(self
        """Standard phone number form"""
        r_ "(%s) %s-%s" %(self.number[:3],
                              self.number[3:6],
                              self.number[6:])

    @staticmethod
    ___ clean(number
        """Tries to identify a phone number"""
        digits = [c for c in number __ c.isdigit()]
        __ le.(digits) __ 11 and digits[0] __ "1":
            r_ ''.join(digits[1:])
        ____ le.(digits) != 10:
            r_ "0000000000"
        ____
            r_ ''.join(digits)
