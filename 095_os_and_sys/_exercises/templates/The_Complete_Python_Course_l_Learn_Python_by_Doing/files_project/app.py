my_file = o..('data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = o..('data.txt', 'w')
my_file_writing.write(user_name)

my_file_writing.close()
