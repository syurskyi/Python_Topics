def non_ascii(word):
    return any(ord(i)>127 for i in word)

def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split() if non_ascii(word)]




print(extract_non_ascii_words('Fichier non trouvé'))

print(non_ascii('trouvé'))