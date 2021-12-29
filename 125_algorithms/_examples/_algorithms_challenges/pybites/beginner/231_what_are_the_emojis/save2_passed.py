import re
from typing import List

def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    return [index
            for (index, emoji) in enumerate(text)
            if re.search((r'[^\w\s,]'), emoji)]