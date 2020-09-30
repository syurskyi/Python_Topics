#Like the previous exercise, but returning a message when the word is not in the dict.
d _ di..(weather _ "clima", earth _ "terra", rain _ "chuva")
___ vocabulary(word):
    try:
        r_ d[word]
    except KeyError:
        r_ "That word does not exist."

word _ input("Enter word: ")
print(vocabulary(word))
