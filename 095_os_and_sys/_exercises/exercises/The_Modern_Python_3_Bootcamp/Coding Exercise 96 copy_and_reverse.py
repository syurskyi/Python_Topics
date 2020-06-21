# Copy and Reverse Solution
#
# copy_and_reverse  is very similar to the previous exercise, copy ,
# except that we reverse the text using a slice before we write it to the new file:


def copy_and_reverse(file_name, new_file_name):
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, "w") as new_file:
        new_file.write(text[::-1])