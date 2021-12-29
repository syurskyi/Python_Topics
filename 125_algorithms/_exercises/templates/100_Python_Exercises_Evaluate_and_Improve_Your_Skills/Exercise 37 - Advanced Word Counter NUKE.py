#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
___ count_words(filepath):
    with open(filepath, 'r') as file:
        string  file.read()
        string  string.r..(",", " ")
        string_list  string.s..(" ")
        r.. l..(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
_______ re

___ count_words_re(filepath):
    with open(filepath, 'r') as file:
        string  file.read()
        string_list  re.s..(",| ", string)
        r.. l..(string_list)

print(count_words_re("words2.txt"))
