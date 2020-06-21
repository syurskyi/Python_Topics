#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.


#!/usr/bin/python

# Import modules for CGI handling 
______ cgi
______ cgitb 

# Create instance of FieldStorage 
form _ cgi.FieldStorage() 

# Get data from fields
name _ form.getvalue('Name')
comment  _ form.getvalue('Comment')

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>CGI Program Example </title>")
print ("</head>")
print ("<body>")
print ("<h2> @ sends a comment: @</h2>"  (name, comment))
print ("</body>")
print ("</html>")
