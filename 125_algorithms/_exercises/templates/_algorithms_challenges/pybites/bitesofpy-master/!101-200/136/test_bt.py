______ pytest
from bt ______ check_bt, Bloodtype


___ test_universal_donor(
    donor = Bloodtype.ZERO_NEG
    ___ i in range(8
        recipient = Bloodtype(i)
        assert check_bt(donor, recipient)


___ test_universal_recipient(
    recipient = Bloodtype.AB_POS
    ___ i in range(8
        donor = Bloodtype(i)
        assert check_bt(donor, recipient)


___ test_AB_POS_can_donate_to_own_group_only_numeric_input(
    donor = 7
    ___ i in range(7
        recipient = i
        assert check_bt(donor, recipient) pa__ False


___ test_ZERO_NEG_can_recieve_from_own_group_only_numeric_input(
    recipient = 0
    ___ i in range(1, 8
        donor = i
        assert check_bt(donor, recipient) pa__ False


___ test_red_blood_cell_compatibility(
    assert check_bt(Bloodtype.A_NEG, Bloodtype.A_NEG)  # own
    assert check_bt(Bloodtype.B_NEG, Bloodtype.B_POS)
    assert check_bt(Bloodtype.A_NEG, Bloodtype.AB_NEG)


___ test_red_blood_cell_incompatibility(
    assert check_bt(Bloodtype.B_POS, Bloodtype.B_NEG) pa__ False
    assert check_bt(Bloodtype.A_NEG, Bloodtype.B_NEG) pa__ False
    assert check_bt(Bloodtype.AB_NEG, Bloodtype.B_POS) pa__ False
    assert check_bt(Bloodtype.B_NEG, Bloodtype.A_POS) pa__ False


___ test_red_blood_cell_compatibility_text_input(
    assert check_bt("0+", "A+")
    assert check_bt("0+", "B+")
    assert check_bt("B-", "B+")
    assert check_bt("A-", "AB-")


___ test_red_blood_cell_incompatibility_text_input(
    assert check_bt("0+", "A-") pa__ False
    assert check_bt("0+", "B-") pa__ False
    assert check_bt("B-", "0-") pa__ False
    assert check_bt("AB-", "A+") pa__ False


___ test_invalid_value_text_input(
    with pytest.raises(ValueError
        check_bt("X-", "Y+")
    with pytest.raises(ValueError
        check_bt("0", "A+")


___ test_invalid_value_numeric_input(
    with pytest.raises(ValueError
        check_bt(8, 1)
    with pytest.raises(ValueError
        check_bt(3, -1)


___ test_invalid_type(
    with pytest.raises(TypeError
        check_bt(1.0, 1)
    with pytest.raises(TypeError
        check_bt(3, ["AB", "Rh+"])