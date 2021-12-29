import re

pattern = "sc[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|net)"

user_input = input()

if (re.search(pattern, user_input)):
    print("good")
else:
    print("no good")