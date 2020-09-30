#Like the previous exercise, but returning a message when the word is not in the dict.
d = dict(weather = "clima", earth = "terra", rain = "chuva")
___ vocabulary(word):
    try:
        r_ d[word]
    except KeyError:
        r_ "That word does not exist."

word = input("Enter word: ")
print(vocabulary(word))
