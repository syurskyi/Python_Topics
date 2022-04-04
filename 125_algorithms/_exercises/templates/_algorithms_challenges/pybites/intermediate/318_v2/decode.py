_______ base64
_______ csv
____ t___ _______ L..  # will remove with 3.9


___ get_credit_cards(data: bytes) __ L..[s..]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    text = base64.decodebytes(data).d.. )
    card_nums = [row.s..(',')[2] ___ row __ text.s.. ]
    card_nums.pop(0)            # remove header

    r.. card_nums
