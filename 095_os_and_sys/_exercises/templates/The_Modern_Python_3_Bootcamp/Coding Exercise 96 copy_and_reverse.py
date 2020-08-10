# Copy and Reverse Solution
#
# copy_and_reverse  is very similar to the previous exercise, copy ,
# except that we reverse the text using a slice before we write it to the new file:


___ copy_and_reverse(file_name, new_file_name):
    w__ o..(file_name) __ file:
        text = file.read()

    w__ o..(new_file_name, "w") __ new_file:
        new_file.w..(text[::-1])