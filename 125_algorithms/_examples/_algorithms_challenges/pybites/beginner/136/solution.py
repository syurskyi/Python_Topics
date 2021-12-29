"""
Check red blood cell compatibility between donor and recipient.
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility
For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:
    pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
    value of the pre-defined Bloodtype 0..7
    pre defined text  e.g. "0-", "B+", "AB+", ...
    If input value is not a required type TypeError is raised.
    If input value is not in defined interval ValueError is raised.
Keywords: enum, exception handling, multi type input
"""

from enum import Enum


class Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


blood_type_text = {
    "0-": Bloodtype.ZERO_NEG,
    "0+": Bloodtype.ZERO_POS,
    "B-": Bloodtype.B_NEG,
    "B+": Bloodtype.B_POS,
    "A-": Bloodtype.A_NEG,
    "A+": Bloodtype.A_POS,
    "AB-": Bloodtype.AB_NEG,
    "AB+": Bloodtype.AB_POS,
}

# possible solution:
def check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """
    donor = _check_convert_input(donor)
    recipient = _check_convert_input(recipient)
    d = donor.value
    r = recipient.value
    anti_gen_comp = (r // 4 % 2 - d // 4 % 2, r // 2 % 2 - d // 2 % 2, r % 2 - d % 2)
    return all(agc >= 0 for agc in anti_gen_comp)


def _check_convert_input(inpval):
    """ Checks onput data type and value,
        if necessary and possible it converts it to Bloodtype.
        Arg:
        inpval (int | str | Bloodtype)
        Returns:
        (Bloodtype): converted (if needed) impval
    """
    if isinstance(inpval, Bloodtype):
        return inpval
    if isinstance(inpval, int):
        if 0 <= inpval <= 7:
            return Bloodtype(inpval)
        else:
            raise ValueError
    if isinstance(inpval, str):
        if inpval in blood_type_text.keys():
            return blood_type_text[inpval]
        else:
            raise ValueError
    else:
        raise TypeError