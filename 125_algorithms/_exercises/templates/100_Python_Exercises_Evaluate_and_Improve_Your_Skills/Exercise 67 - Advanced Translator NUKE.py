#Like the previous exercise, but returning a message when the word is not in the dict.
d  d..(weather  "clima", earth  "terra", rain  "chuva")
___ vocabulary(word):
    ___
        r.. d[word]
    ______ KeyError:
        r.. "That word does not exist."

word  input("Enter word: ")
print(vocabulary(word))
