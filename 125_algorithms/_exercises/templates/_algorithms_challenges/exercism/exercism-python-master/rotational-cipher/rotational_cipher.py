___ rotate(text, key
    ___ rot(letter
        __ letter.islower(
            r_ chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
        __ letter.isupper(
            r_ chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
        r_ letter
    r_ ''.join(rot(l) ___ l in text)
