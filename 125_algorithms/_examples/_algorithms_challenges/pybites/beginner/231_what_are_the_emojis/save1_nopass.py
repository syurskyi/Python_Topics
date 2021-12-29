import re
from typing import List

def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    emoji = re.findall(re.compile(r'[^\w\s,]'), text)
    return [text.index(e) for e in emoji if e in text]