#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
___ count_words(filepath):
    w__ open(filepath, 'r') __ file:
        s__  file.read()
        s__  s__.r..(",", " ")
        string_list  s__.s..(" ")
        r.. l..(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
_______ __

___ count_words_re(filepath):
    w__ open(filepath, 'r') __ file:
        s__  file.read()
        string_list  __.s..(",| ", s__)
        r.. l..(string_list)

print(count_words_re("words2.txt"))
