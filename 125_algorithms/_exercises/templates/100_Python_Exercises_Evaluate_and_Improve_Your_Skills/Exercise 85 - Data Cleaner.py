#Create a script cleans the countries_raw.txt file from unecessary lines and leaves countries only

with open("countries_raw.txt", "r") as file:
    content = file.readlines()


content = [i.strip("\n") ___ i __ content if "\n" __ i]

content = [i ___ i __ content if i !=""]
content = [i ___ i __ content if i !="Top of Page"]

content = [i ___ i __ content if len(i) != 1]
print(content)


with open("countries_clean.txt", "w") as file:
    ___ i __ content:
        file.write(i+"\n")
