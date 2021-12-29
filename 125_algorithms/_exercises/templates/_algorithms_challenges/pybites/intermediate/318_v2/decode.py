_______ base64
_______ csv
____ typing _______ List  # will remove with 3.9


___ get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    text = base64.decodebytes(data).decode()
    card_nums = [row.split(',')[2] ___ row __ text.splitlines()]
    card_nums.pop(0)            # remove header

    r.. card_nums
