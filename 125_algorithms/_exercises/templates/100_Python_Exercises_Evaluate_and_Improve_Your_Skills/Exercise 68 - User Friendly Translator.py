#Like the previous exercise, but considering user may enter different letter cases
d _ di..(weather _ "clima", earth _ "terra", rain _ "chuva")
___ vocabulary(word):
    try:
        r_ d[word]
    except KeyError:
        r_ "That word does not exist."

word _ input("Enter word: ").l..
print(vocabulary(word))
