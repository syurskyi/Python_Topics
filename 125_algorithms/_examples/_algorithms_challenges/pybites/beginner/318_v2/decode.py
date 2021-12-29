import base64
import csv
from typing import List  # will remove with 3.9
from io import StringIO
import pandas as pd



def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """

    decoded = base64.b64decode(data)
    message = decoded.decode('ascii')

    return pd.read_csv(StringIO(message),usecols=['credit_card'],squeeze=True).astype(str).tolist()




