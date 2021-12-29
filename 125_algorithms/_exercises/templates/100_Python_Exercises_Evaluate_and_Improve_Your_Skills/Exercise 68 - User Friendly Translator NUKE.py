#Like the previous exercise, but considering user may enter different letter cases
d  d..(weather  "clima", earth  "terra", rain  "chuva")
___ vocabulary(word):
    try:
        r.. d[word]
    except KeyError:
        r.. "That word does not exist."

word  input("Enter word: ").l..
print(vocabulary(word))
