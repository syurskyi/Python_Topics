s = 'a\nb\tc'

print(s)
print(s)

print(len(s))

s = '\001\002\x03'
print(s)

print(len(s))

S = "s\tp\na\x00m"
print(S)
print(len(S))
print(S)

x = "C:\py\code"  # Keeps \ literally (and displays it as \\)
print(x)
print(len(x))