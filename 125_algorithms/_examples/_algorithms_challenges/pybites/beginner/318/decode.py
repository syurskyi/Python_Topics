import base64
import csv
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    temp_list = []
    for each_name in base64.standard_b64decode(data).splitlines():
        cc = each_name.decode('utf-8').split(',')[2]
        if cc.isnumeric():
            temp_list.append(cc)
    return temp_list
