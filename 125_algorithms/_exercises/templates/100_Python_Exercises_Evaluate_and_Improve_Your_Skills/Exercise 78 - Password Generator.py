#When writing web apps, you may need to generate default random passwords for users.
#Create a program that generates a password of 6 random alphanumeric characters in the range abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?

______ random

characters _ "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen _ random.sample(characters, 6)
password _ "".join(chosen)
print(password)


#Video question -Easy
