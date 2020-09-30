#Create a script cleans the countries_raw.txt file from unecessary lines and leaves countries only

with open("countries_raw.txt", "r") as file:
    content _ file.readlines()


content _ [i.strip("\n") ___ i __ content __ "\n" __ i]

content _ [i ___ i __ content __ i !_""]
content _ [i ___ i __ content __ i !_"Top of Page"]

content _ [i ___ i __ content __ le.(i) !_ 1]
print(content)


with open("countries_clean.txt", "w") as file:
    ___ i __ content:
        file.write(i+"\n")
