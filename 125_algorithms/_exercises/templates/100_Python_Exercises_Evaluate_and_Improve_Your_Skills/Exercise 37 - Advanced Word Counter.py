#Create a function like in the previous exercise, but taking into consideration that commas without space can separate words.
___ count_words(filepath):
    w__ o..(filepath, 'r') __ file:
        string _ file.r__
        string _ string.replace(",", " ")
        string_list _ string.split(" ")
        r_ le.(string_list)

print(count_words("words2.txt"))

#Other solution using regular expressions
______ __

___ count_words_re(filepath):
    w__ o..(filepath, 'r') __ file:
        string _ file.r__
        string_list _ __.split(",| ", string)
        r_ le.(string_list)

print(count_words_re("words2.txt"))
