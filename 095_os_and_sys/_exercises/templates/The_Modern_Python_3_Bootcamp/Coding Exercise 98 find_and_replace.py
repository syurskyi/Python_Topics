___ find_and_replace(file_name, old_word, new_word):
    w__ o..(file_name, "r+") __ file:
        text _ file.read()
        new_text _ text.replace(old_word, new_word)
        file.seek(0)
        file.w..(new_text)
        file.truncate()

