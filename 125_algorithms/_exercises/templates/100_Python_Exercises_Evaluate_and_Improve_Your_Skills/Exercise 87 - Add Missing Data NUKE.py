#Add the missing items to the file

checklist  ["Portugal", "Germany", "Spain"]
checklist  [i + "\n" ___ i __ checklist]

w__ open("countries_missing.txt", "r") __ file:
    content  file.r..
print(checklist + content)

updated_list  s..(checklist + content)

w__ open("countries_missing_fixed.txt", "w") __ file:
    ___ i __ updated_list:
        file.write(i)
