import base64
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    decoded_data = base64.b64decode(data)
    decoded_string = decoded_data.decode("ascii")
    decoded_list = [row.split(",") for row in decoded_string.strip().split("\n")]
    credit_card_numbers = [decoded_list[i][2] for i in range(len(decoded_list)) if i != 0]
    return credit_card_numbers