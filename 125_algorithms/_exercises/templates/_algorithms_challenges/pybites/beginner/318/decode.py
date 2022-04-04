_______ base64
_______ csv
____ t___ _______ List  # will remove with 3.9


___ get_credit_cards(data: bytes) __ List[s..]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    temp_list    # list
    ___ each_name __ base64.standard_b64decode(data).s..
        cc = each_name.d.. 'utf-8').s..(',')[2]
        __ cc.isnumeric
            temp_list.a..(cc)
    r.. temp_list
