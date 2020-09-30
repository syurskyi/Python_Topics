#Create a script that checks a list against countries_clean.txt
#and creates a list with items that were in that file

checklist _ ["Portugal", "Germany", "Munster", "Spain"]

with open("countries_clean.txt", "r") as file:
    content _ file.readlines()

content _ [i.rstrip('\n') ___ i __ content]
checked _ [i ___ i __ content __ i __ checklist]

print(checked)
