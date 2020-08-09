from collections ______ Counter


___ word_count(text
    ___ replace_nonalpha(char
        r_ char.lower() __ char.isalnum() else ' '
    text = ''.join(replace_nonalpha(c) for c in text)
    r_ Counter(text.split())
