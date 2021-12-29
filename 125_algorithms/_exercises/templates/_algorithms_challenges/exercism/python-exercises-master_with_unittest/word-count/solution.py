____ collections _______ Counter


___ word_count(text):
    ___ replace_nonalpha(char):
        r.. char.lower() __ char.isalnum() ____ ' '
    text = ''.join(replace_nonalpha(c) ___ c __ text)
    r.. Counter(text.s..())
