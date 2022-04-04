_______ base64
____ t___ _______ List  # will remove with 3.9


___ get_credit_cards(data: bytes) __ List[s..]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    decoded_data = base64.b64decode(data)
    decoded_string = decoded_data.d.. "ascii")
    decoded_list = [row.s..(",") ___ row __ decoded_string.s...s..("\n")]
    credit_card_numbers = [decoded_list[i][2] ___ i __ r..(l..(decoded_list)) __ i != 0]
    r.. credit_card_numbers