___ extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    na_words    # list
    ___ word __ text.s..(" "):
        word_split = l..(word)
        ___ letter __ word_split:
            __ ord(letter) >= 128:
                na_words.a..(word)
                break
    r.. na_words


# if __name__ == "__main__":
#     print(extract_non_ascii_words("He wonede at Ernleȝe at æðelen are chirechen"))
#     print(extract_non_ascii_words('Over \u0e55\u0e57 57 flavours'))