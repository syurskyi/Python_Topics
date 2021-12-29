def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    na_words = []
    for word in text.split(" "):
        word_split = list(word)
        for letter in word_split:
            if ord(letter) >= 128:
                na_words.append(word)
                break
    return na_words


# if __name__ == "__main__":
#     print(extract_non_ascii_words("He wonede at Ernleȝe at æðelen are chirechen"))
#     print(extract_non_ascii_words('Over \u0e55\u0e57 57 flavours'))