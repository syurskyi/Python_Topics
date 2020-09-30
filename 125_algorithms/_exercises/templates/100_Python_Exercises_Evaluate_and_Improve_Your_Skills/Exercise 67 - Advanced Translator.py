#Like the previous exercise, but returning a message when the word is not in the dict.
d _ di..(weather _ "clima", earth _ "terra", rain _ "chuva")
___ vocabulary(word):
    ___
        r_ d[word]
    ______ KeyError:
        r_ "That word does not exist."

word _ input("Enter word: ")
print(vocabulary(word))
