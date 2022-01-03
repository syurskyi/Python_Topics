_______ base64
_______ csv
____ typing _______ List  # will remove with 3.9
____ io _______ StringIO
_______ pandas as pd



___ get_credit_cards(data: bytes) -> List[s..]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """

    decoded = base64.b64decode(data)
    message = decoded.decode('ascii')

    r.. pd.read_csv(StringIO(message),usecols=['credit_card'],squeeze=T..).astype(s..).tolist()




