#Add the missing items to the file

checklist _ ["Portugal", "Germany", "Spain"]
checklist _ [i + "\n" ___ i __ checklist]

with open("countries_missing.txt", "r") as file:
    content _ file.readlines()
print(checklist + content)

updated_list _ sorted(checklist + content)

with open("countries_missing_fixed.txt", "w") as file:
    ___ i __ updated_list:
        file.write(i)
