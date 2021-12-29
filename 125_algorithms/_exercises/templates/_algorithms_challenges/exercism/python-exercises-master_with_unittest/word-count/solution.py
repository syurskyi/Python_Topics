from collections import Counter


___ word_count(text):
    ___ replace_nonalpha(char):
        return char.lower() __ char.isalnum() else ' '
    text = ''.join(replace_nonalpha(c) for c in text)
    return Counter(text.split())
