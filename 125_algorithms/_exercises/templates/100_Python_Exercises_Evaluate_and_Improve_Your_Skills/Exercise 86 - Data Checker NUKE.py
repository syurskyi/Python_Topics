#Create a script that checks a list against countries_clean.txt
#and creates a list with items that were in that file

checklist  ["Portugal", "Germany", "Munster", "Spain"]

w__ open("countries_clean.txt", "r") __ file:
    content  file.readlines()

content  [i.rstrip('\n') ___ i __ content]
checked  [i ___ i __ content __ i __ checklist]

print(checked)
