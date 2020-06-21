records = [bytes([char] * 8) for char in b'spam']
records
# [b'ssssssss', b'pppppppp', b'aaaaaaaa', b'mmmmmmmm']
# ######################################################################################################################

file = open('random.bin', 'w+b')
>for rec in records: # write four records
    size = file.write(rec) # bytes for binary mode

file.flush()
pos = file.seek(0) # read entire file
print(file.read())
# b'ssssssssppppppppaaaaaaaammmmmmmm'
# ######################################################################################################################

file = open('random.bin', 'r+b')
print(file.read()) # read entire file
# b'ssssssssppppppppaaaaaaaammmmmmmm'
# ######################################################################################################################

record = b'X' * 8
file.seek(0) # update first record
file.write(record)
file.seek(len(record) * 2) # update third record
file.write(b'Y' * 8)
file.seek(8)
file.read(len(record)) # fetch second record
# b'pppppppp'
# ######################################################################################################################

file.read(len(record)) # fetch next (third) record
# b'YYYYYYYY'
# ######################################################################################################################

file.seek(0) # read entire file
file.read()
# b'XXXXXXXXppppppppYYYYYYYYmmmmmmmm'
# c:\temp> type random.bin # the view outside Python
# XXXXXXXXppppppppYYYYYYYYmmmmmmmm
# ######################################################################################################################

# c:\temp> python
file = open('random.bin', 'r') # text mode ok if no encoding/endlines
reclen = 8
file.seek(reclen * 3) # fetch record 4
file.read(reclen)
# 'mmmmmmmm'
# ######################################################################################################################

file.seek(reclen * 1) # fetch record 2
file.read(reclen)

# 'pppppppp'
file = open('random.bin', 'rb') # binary mode works the same here
file.seek(reclen * 2) # fetch record 3
file.read(reclen) # returns byte strings
# b'YYYYYYYY'
# ######################################################################################################################

data = 'sp\xe4m' # data to your script
data, len(data) # 4 unicode chars, 1 nonascii
# ('späm', 4)
# ######################################################################################################################

data.encode('utf8'), len(data.encode('utf8')) # bytes written to file
# (b'sp\xc3\xa4m', 5)
# ######################################################################################################################

f = open('test', mode='w+', encoding='utf8') # use text mode, encoded
f.write(data)
f.flush()
f.seek(0); f.read(1) # ascii bytes work
# 's'
# ######################################################################################################################

f.seek(2); f.read(1) # as does 2-byte nonascii
#'ä'
# ######################################################################################################################

data[3] # but offset 3 is not 'm' !
# 'm'
# ######################################################################################################################

f.seek(3); f.read(1)
# UnicodeDecodeError: 'utf8' codec can't decode byte 0xa4 in position 0:
# unexpected code byte
# ######################################################################################################################