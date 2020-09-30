#Clean each line by removing s from https and adding a slash

w__ o..("urls.txt", "r") __ file:
    lines _ file.r_l_()

print(lines)

w__ o..("urls_corrected.txt", _) __ file:
    ___ line __ lines:
        line_remove_s _ line.replace("s", "", 1)
        print(line_remove_s)
        line_remove_s_add_slash _ line_remove_s[:6] + "/" + line_remove_s[6:]
        print(line_remove_s_add_slash)
        file.w..(line_remove_s_add_slash)
