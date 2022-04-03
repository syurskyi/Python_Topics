_______ p__
____ bt _______ check_bt, Bloodtype


___ test_universal_donor
    donor = Bloodtype.ZERO_NEG
    ___ i __ r..(8
        recipient = Bloodtype(i)
        ... check_bt(donor, recipient)


___ test_universal_recipient
    recipient = Bloodtype.AB_POS
    ___ i __ r..(8
        donor = Bloodtype(i)
        ... check_bt(donor, recipient)


___ test_AB_POS_can_donate_to_own_group_only_numeric_input
    donor = 7
    ___ i __ r..(7
        recipient = i
        ... check_bt(donor, recipient) __ F..


___ test_ZERO_NEG_can_recieve_from_own_group_only_numeric_input
    recipient = 0
    ___ i __ r..(1, 8
        donor = i
        ... check_bt(donor, recipient) __ F..


___ test_red_blood_cell_compatibility
    ... check_bt(Bloodtype.A_NEG, Bloodtype.A_NEG)  # own
    ... check_bt(Bloodtype.B_NEG, Bloodtype.B_POS)
    ... check_bt(Bloodtype.A_NEG, Bloodtype.AB_NEG)


___ test_red_blood_cell_incompatibility
    ... check_bt(Bloodtype.B_POS, Bloodtype.B_NEG) __ F..
    ... check_bt(Bloodtype.A_NEG, Bloodtype.B_NEG) __ F..
    ... check_bt(Bloodtype.AB_NEG, Bloodtype.B_POS) __ F..
    ... check_bt(Bloodtype.B_NEG, Bloodtype.A_POS) __ F..


___ test_red_blood_cell_compatibility_text_input
    ... check_bt("0+", "A+")
    ... check_bt("0+", "B+")
    ... check_bt("B-", "B+")
    ... check_bt("A-", "AB-")


___ test_red_blood_cell_incompatibility_text_input
    ... check_bt("0+", "A-") __ F..
    ... check_bt("0+", "B-") __ F..
    ... check_bt("B-", "0-") __ F..
    ... check_bt("AB-", "A+") __ F..


___ test_invalid_value_text_input
    w__ p__.r..(V...
        check_bt("X-", "Y+")
    w__ p__.r..(V...
        check_bt("0", "A+")


___ test_invalid_value_numeric_input
    w__ p__.r..(V...
        check_bt(8, 1)
    w__ p__.r..(V...
        check_bt(3, -1)


___ test_invalid_type
    w__ p__.r.. T..
        check_bt(1.0, 1)
    w__ p__.r.. T..
        check_bt(3, ["AB", "Rh+"])
