"""
Write a function which checks the red blood cell compatibility between donor and recipient.
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

# complete :
def check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
    """

    if type(donor) is int and (donor < 0 or donor > 7):
        raise ValueError
    elif type(donor) is float:
        raise TypeError
    elif type(donor) is str:
        if donor in blood_type_text:
            donor = blood_type_text[donor].value
        else:
            raise ValueError
    elif type(donor) is Bloodtype:
        donor = donor.value

    
    if type(recipient) is int and (recipient < 0 or recipient > 7):
        raise ValueError
    elif type(recipient) is float:
        raise TypeError
    elif type(recipient) is str:
        if recipient in blood_type_text:
            recipient = blood_type_text[recipient].value
        else:
            raise ValueError
    elif type(recipient) is Bloodtype:
        recipient = recipient.value

    print(donor, recipient)
    temp = _particular_antigen_comp(donor, recipient)
    return not len([n for n in temp if n < 0 ])




# hint
def _particular_antigen_comp(donor: int, recipient: int) -> tuple:
    """Returns a particalar antigen compatibility, where each tuple member
    marks a compatibility for a particular antigen  (A, B, Rh-D).
    If tuple member is non-negative there is a compatibility.
    For red blood cell compatibility is required that 
    all tuple members are non-negative (i.e. compatibility for all 3 antigens).
    0- bloodtype is represented as 0 ; AB+ is represented as 7; see Bloodtype enum
    Examples:
    _particular_antigen_comp(0, 7) -> (1, 1, 1)    0- can donate to AB+
    _particular_antigen_comp(1, 3) -> (0, 1, 0)    0+ can donate to B+
    _particular_antigen_comp(2, 5) -> (1, -1, 1)   B+ cannot donate to A+
    _particular_antigen_comp(7, 0) -> (-1, -1, -1) AB+ cannot donate to 0-
    """
    return (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )




#donor = Bloodtype.ZERO_NEG
#print(type(donor))
#print(type(Bloodtype.A_NEG))
#for i in range(8):
#    print(_particular_antigen_comp(0, i))

#
print(check_bt( Bloodtype.ZERO_NEG, Bloodtype.ZERO_NEG))

#print(check_bt( Bloodtype.ZERO_NEG, Bloodtype.ZERO_NEG))
#print(check_bt(Bloodtype.ZERO_NEG,2))
""" donor = 7
for i in range(7):
    recipient = i
    print(check_bt(donor, recipient)) """

print(check_bt(7, 0))