from re ______ findall

___ encode(text
    """encode compresses text by replacing repeated characters
    with number of repeates and the character"""
    r_ ''.join(
        "%d%s" % (le.(letters), letter) __ le.(letters) > 1 else letter
        ___ letters, letter in findall(r'((.)\2*)', text))

___ decode(compressed
    """decode uncompresses text but expanding repeated characters"""
    r_ ''.join(
        int(count) * letter __ count else letter
        ___ count, letter in findall('(\d*)(.)', compressed ))
