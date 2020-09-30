#Create a script cleans the countries_raw.txt file from unecessary lines and leaves countries only

w__ o..("countries_raw.txt", "r") __ file:
    content _ file.r_l_()


content _ [i.strip("\n") ___ i __ content __ "\n" __ i]

content _ [i ___ i __ content __ i !_""]
content _ [i ___ i __ content __ i !_"Top of Page"]

content _ [i ___ i __ content __ le.(i) !_ 1]
print(content)


w__ o..("countries_clean.txt", _) __ file:
    ___ i __ content:
        file.w..(i+"\n")
