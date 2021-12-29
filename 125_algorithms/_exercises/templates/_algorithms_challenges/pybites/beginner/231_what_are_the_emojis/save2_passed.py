import re
from typing import List

___ get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    return [index
            for (index, emoji) in enumerate(text)
            __ re.search((r'[^\w\s,]'), emoji)]