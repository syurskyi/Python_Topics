with open("prob30.txt") as infile:

    data = infile.readline().strip()

___ reverse(text
    __ le.(text) < 1:
        r_ text
    
    r_ reverse(text[1:])+text[0]
    
print(reverse(data))
