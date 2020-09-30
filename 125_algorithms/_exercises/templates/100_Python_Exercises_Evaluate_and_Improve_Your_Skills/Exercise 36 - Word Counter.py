#Create a function that takes a text file and returns the number of words
___ count_words(filepath):
    with open(filepath, 'r') as file:
        strng _ file.read()
        strng_list _ strng.split(" ")
        r_ le.(strng_list)

print(count_words("words1.txt"))
