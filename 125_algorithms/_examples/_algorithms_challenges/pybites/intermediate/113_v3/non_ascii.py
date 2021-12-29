def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""

    words = text.split()

    result = []
    for word in words:
        try:
            word.encode('ascii')
        except Exception as e:
            print(e)
            result.append(word)


    return result


