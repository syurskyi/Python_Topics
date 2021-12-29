import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    return [i for i in range(len(text)) if IS_EMOJI.match(text,i)]
    #for i in range(len(text)):
    #    if IS_EMOJI.match(text, i):
    #        print(i)
    #    #print(IS_EMOJI.search(char))

print(get_emoji_indices('We 💜 Python 🐍'))