#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
___ count_words(filepath):
    with open(filepath, 'r') as file:
        string _ file.read()
        string _ string.replace(",", " ")
        string_list _ string.split(" ")
        r_ le.(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
______ re

___ count_words_re(filepath):
    with open(filepath, 'r') as file:
        string _ file.read()
        string_list _ re.split(",| ", string)
        r_ le.(string_list)

print(count_words_re("words2.txt"))
