_______ pytest
____ bt _______ check_bt, Bloodtype


___ test_universal_donor():
    donor = Bloodtype.ZERO_NEG
    ___ i __ r..(8):
        recipient = Bloodtype(i)
        ... check_bt(donor, recipient)


___ test_universal_recipient():
    recipient = Bloodtype.AB_POS
    ___ i __ r..(8):
        donor = Bloodtype(i)
        ... check_bt(donor, recipient)


___ test_AB_POS_can_donate_to_own_group_only_numeric_input():
    donor = 7
    ___ i __ r..(7):
        recipient = i
        ... check_bt(donor, recipient) __ False


___ test_ZERO_NEG_can_recieve_from_own_group_only_numeric_input():
    recipient = 0
    ___ i __ r..(1, 8):
        donor = i
        ... check_bt(donor, recipient) __ False


___ test_red_blood_cell_compatibility():
    ... check_bt(Bloodtype.A_NEG, Bloodtype.A_NEG)  # own
    ... check_bt(Bloodtype.B_NEG, Bloodtype.B_POS)
    ... check_bt(Bloodtype.A_NEG, Bloodtype.AB_NEG)


___ test_red_blood_cell_incompatibility():
    ... check_bt(Bloodtype.B_POS, Bloodtype.B_NEG) __ False
    ... check_bt(Bloodtype.A_NEG, Bloodtype.B_NEG) __ False
    ... check_bt(Bloodtype.AB_NEG, Bloodtype.B_POS) __ False
    ... check_bt(Bloodtype.B_NEG, Bloodtype.A_POS) __ False


___ test_red_blood_cell_compatibility_text_input():
    ... check_bt("0+", "A+")
    ... check_bt("0+", "B+")
    ... check_bt("B-", "B+")
    ... check_bt("A-", "AB-")


___ test_red_blood_cell_incompatibility_text_input():
    ... check_bt("0+", "A-") __ False
    ... check_bt("0+", "B-") __ False
    ... check_bt("B-", "0-") __ False
    ... check_bt("AB-", "A+") __ False


___ test_invalid_value_text_input():
    with pytest.raises(ValueError):
        check_bt("X-", "Y+")
    with pytest.raises(ValueError):
        check_bt("0", "A+")


___ test_invalid_value_numeric_input():
    with pytest.raises(ValueError):
        check_bt(8, 1)
    with pytest.raises(ValueError):
        check_bt(3, -1)


___ test_invalid_type():
    with pytest.raises(TypeError):
        check_bt(1.0, 1)
    with pytest.raises(TypeError):
        check_bt(3, ["AB", "Rh+"])
