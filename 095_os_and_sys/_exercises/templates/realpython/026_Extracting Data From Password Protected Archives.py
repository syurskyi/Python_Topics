# zipfile supports extracting password protected ZIPs. To extract password protected ZIP files, pass in the password
# to the .extract() or .extractall() method as an argument:
#
______ zipfile

w__ zipfile.ZipFile('secret.zip', 'r') __ pwd_zip:
    # Extract from a password protected archive
    pwd_zip.extractall(p..='extract_dir', pwd='Quish3@o')
#
# This opens the secret.zip archive in read mode. A password is supplied to .extractall(), and the archive contents
# are extracted to extract_dir. The archive is closed automatically after the extraction is complete thanks
# to the with statement.

