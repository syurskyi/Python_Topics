def append_letter(lst, letter):
    for i in range(len(lst)):
        lst[i] += letter

# Initial List
word_list = ["Hello", "World", "!"]

# Pass the list to the function
append_letter(word_list, "z")

# See the modified list.
# It's the same list object in memory
print(word_list)
