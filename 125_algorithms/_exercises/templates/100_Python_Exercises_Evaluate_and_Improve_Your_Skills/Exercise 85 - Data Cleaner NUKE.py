#Create a script cleans the countries_raw.txt file from unecessary lines and leaves countries only

with open("countries_raw.txt", "r") __ file:
    content  file.readlines()


content  [i.strip("\n") ___ i __ content __ "\n" __ i]

content  [i ___ i __ content __ i !""]
content  [i ___ i __ content __ i !"Top of Page"]

content  [i ___ i __ content __ l..(i) ! 1]
print(content)


with open("countries_clean.txt", "w") __ file:
    ___ i __ content:
        file.write(i+"\n")
