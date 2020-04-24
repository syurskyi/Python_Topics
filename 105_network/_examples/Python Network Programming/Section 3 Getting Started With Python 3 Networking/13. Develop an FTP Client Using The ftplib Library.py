import ftplib
import os


def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
    except:
        print("Error")


def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)


ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")

data = []

# change directory to /pub/
ftp.cwd('/pub/')
ftp.dir(data.append)
for line in data:
    print("-", line)

print("Downloading README.nluug")
getFile(ftp, 'README.nluug')
print("Download complete")
print("Uploading README.nluug")
try:
    upload(ftp, "README.nluug")
except:
    print("Failed to upload README.nluug")

ftp.quit()
