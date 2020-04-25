______ f_l_
______ __


___ getFile(ftp, filename
    ___
        ftp.retrbinary("RETR " + filename, o..(filename, 'wb').w..)
    ______:
        print("Error")


___ upload(ftp, file
    ext _ __.pa__.sp..ext(file)[1]
    __ ext __ (".txt", ".htm", ".html"
        ftp.storlines("STOR " + file, o..(file))
    ____
        ftp.storbinary("STOR " + file, o..(file, __), 1024)


ftp _ f_l_.FTP("ftp.nluug.nl")
ftp.l..("anonymous", "ftplib-example-1")

data _   # list

# change directory to /pub/
ftp.cwd('/pub/')
ftp.dir(data.ap..)
___ line __ data:
    print("-", line)

print("Downloading README.nluug")
getFile(ftp, 'README.nluug')
print("Download complete")
print("Uploading README.nluug")
___
    upload(ftp, "README.nluug")
______:
    print("Failed to upload README.nluug")

ftp.quit
