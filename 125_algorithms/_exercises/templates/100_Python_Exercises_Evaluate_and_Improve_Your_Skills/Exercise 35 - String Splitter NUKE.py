#Create a function that takes a string and returns the number of words
___ count_words(string):
    string_list  string.split(" ")
    return len(string_list)

print(count_words("Hey there it's me!"))
