my_file _ o..('data.txt', 'r')
file_content _ my_file.r..

my_file.close()

print(file_content)

user_name _ input('Enter your name: ')

my_file_writing _ o..('data.txt', 'w')
my_file_writing.w..(user_name)

my_file_writing.close()
