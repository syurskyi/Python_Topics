# # zipfile supports extracting password protected ZIPs. To extract password protected ZIP files, pass in the password
# # to the .extract() or .extractall() method as an argument:
# #
# ______ z_f_
#
# w__ z_f_.ZF.. 'secret.zip' _ __ pwd_zip
#     # Extract from a password protected archive
#     ?.e_a.. p.._'extract_dir' p.._'Quish3@o'
# #
# # This opens the secret.zip archive in read mode. A password is supplied to .extractall(), and the archive contents
# # are extracted to extract_dir. The archive is closed automatically after the extraction is complete thanks
# # to the with statement.
#
