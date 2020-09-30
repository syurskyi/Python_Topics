#Create a script that checks a list against countries_clean.txt
#and creates a list with items that were in that file

checklist _ ["Portugal", "Germany", "Munster", "Spain"]

w__ o..("countries_clean.txt", "r") __ file:
    content _ file.r_l_()

content _ [i.rstrip('\n') ___ i __ content]
checked _ [i ___ i __ content __ i __ checklist]

print(checked)
