_______ re
____ typing _______ List

___ get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    emoji = re.findall(re.compile(r'[^\w\s,]'), text)
    r.. [text.index(e) ___ e __ emoji __ e __ text]