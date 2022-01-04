#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
___ count_words(filepath):
    w__ open(filepath, 'r') __ file:
        string  file.read()
        string  string.r..(",", " ")
        string_list  string.s..(" ")
        r.. l..(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
_______ __

___ count_words_re(filepath):
    w__ open(filepath, 'r') __ file:
        string  file.read()
        string_list  __.s..(",| ", string)
        r.. l..(string_list)

print(count_words_re("words2.txt"))
