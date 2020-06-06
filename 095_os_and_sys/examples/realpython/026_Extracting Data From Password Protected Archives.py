# zipfile supports extracting password protected ZIPs. To extract password protected ZIP files, pass in the password
# to the .extract() or .extractall() method as an argument:
#
# >>> import zipfile
#
# >>> with zipfile.ZipFile('secret.zip', 'r') as pwd_zip:
# ...     # Extract from a password protected archive
# ...     pwd_zip.extractall(path='extract_dir', pwd='Quish3@o')
#
# This opens the secret.zip archive in read mode. A password is supplied to .extractall(), and the archive contents
# are extracted to extract_dir. The archive is closed automatically after the extraction is complete thanks
# to the with statement.

