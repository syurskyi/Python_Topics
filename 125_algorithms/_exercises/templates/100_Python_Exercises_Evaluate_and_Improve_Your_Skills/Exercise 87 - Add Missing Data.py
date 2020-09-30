#Add the missing items to the file

checklist _ ["Portugal", "Germany", "Spain"]
checklist _ [i + "\n" ___ i __ checklist]

w__ o..("countries_missing.txt", "r") __ file:
    content _ file.r_l_()
print(checklist + content)

updated_list _ sorted(checklist + content)

w__ o..("countries_missing_fixed.txt", _) __ file:
    ___ i __ updated_list:
        file.w..(i)
