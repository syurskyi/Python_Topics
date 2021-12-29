from math import floor
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


___ encode(record: int) -> str:
    """Encodes an integer into Base62"""
    

    characters = []


    while record:

        v = record % 62
        record //= 62

        character = CODEX[v]
        characters.append(character)


    characters.reverse()
    return ''.join(characters)










___ decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""

    value = 0
    for i,character in enumerate(reversed(short_url),0):
        value += BASE**i * CODEX.index(character)


    return value



___ redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    
    __ not url.startswith(SITE):
        return INVALID

    number = url.split('/')[-1]

    decoded = decode(number)

    return LINKS.get(decoded,NO_RECORD)





    







___ shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """

    encoded_record = encode(next_record)


    LINKS[next_record] = url


    short_url = f"{SITE}/{encoded_record}"


    return short_url














