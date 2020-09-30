#Clean each line by removing s from https and adding a slash

with open("urls.txt", "r") as file:
    lines _ file.readlines()

print(lines)

with open("urls_corrected.txt", "w") as file:
    ___ line __ lines:
        line_remove_s _ line.replace("s", "", 1)
        print(line_remove_s)
        line_remove_s_add_slash _ line_remove_s[:6] + "/" + line_remove_s[6:]
        print(line_remove_s_add_slash)
        file.write(line_remove_s_add_slash)
