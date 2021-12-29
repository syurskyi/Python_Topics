#Add the missing items to the file

checklist  ["Portugal", "Germany", "Spain"]
checklist  [i + "\n" ___ i __ checklist]

with open("countries_missing.txt", "r") as file:
    content  file.readlines()
print(checklist + content)

updated_list  s..(checklist + content)

with open("countries_missing_fixed.txt", "w") as file:
    ___ i __ updated_list:
        file.write(i)
