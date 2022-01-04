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

____ enum _______ Enum


c_ Bloodtype(Enum):
    ZERO_NEG = 0
    ZERO_POS = 1
    B_NEG = 2
    B_POS = 3
    A_NEG = 4
    A_POS = 5
    AB_NEG = 6
    AB_POS = 7


    ___ __lte__(self,other):


        r.. i..(self) <= i..(other)



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
___ check_bt(donor, recipient):
    """ Checks red blood cell compatibility based on 8 blood types
        Args:
        donor (int | str | Bloodtype): red blood cell type of the donor
        recipient (int | str | Bloodtype): red blood cell type of the recipient
        Returns:
        bool: True for compatability, False otherwise.
        
    """
    
    
    ___ blood_type __ (donor,recipient):
        __ t..(blood_type) n.. __ (s..,i..,Bloodtype):
            raise TypeError("Invalid types")
    


    blood_types    # list
    ___ blood_type __ (donor,recipient):
        __ t..(blood_type) __ s..:
            __ blood_type n.. __ blood_type_text:
                raise ValueError
            blood_types.a..(blood_type_text[blood_type])
        ____ t..(blood_type) __ i..:
            blood_types.a..(Bloodtype(blood_type))
        ____:
            blood_types.a..(blood_type)
        



    donor,recipient = blood_types

    

    __ recipient __ Bloodtype.ZERO_NEG:
        r.. donor __ Bloodtype.ZERO_NEG
    ____ recipient __ Bloodtype.ZERO_POS:
        r.. donor.value <= Bloodtype.ZERO_POS.value
    ____ recipient __ Bloodtype.B_NEG:
        r.. donor __ (Bloodtype.ZERO_NEG,Bloodtype.B_NEG)
    ____ recipient __ Bloodtype.B_POS:
        r.. donor.value <= Bloodtype.B_POS.value
    ____ recipient __ Bloodtype.A_NEG:
        r.. donor __ (Bloodtype.ZERO_NEG,Bloodtype.A_NEG)
    ____ recipient __ Bloodtype.A_POS:
        r.. donor __ (Bloodtype.ZERO_NEG,Bloodtype.ZERO_POS,Bloodtype.A_NEG,Bloodtype.A_POS)
    ____ recipient __ Bloodtype.AB_NEG:
        r.. donor __ (Bloodtype.ZERO_NEG,Bloodtype.A_NEG,Bloodtype.A_POS)
    ____:
        r.. T..


    r.. F..
    

    


# hint
___ _particular_antigen_comp(donor: i.., recipient: i..) __ tuple:
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
    r.. (
        ((recipient // 4) % 2) - ((donor // 4) % 2),
        ((recipient // 2) % 2) - ((donor // 2) % 2),
        (recipient % 2) - (donor % 2),
    )
