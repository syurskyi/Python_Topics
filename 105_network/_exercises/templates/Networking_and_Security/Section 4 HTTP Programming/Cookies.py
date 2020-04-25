_____ _2

url _ "https://www.google.com"
request _ _2.R..(url)
resp _ _2.u_o..(request)
cookies _ resp.info['Set-Cookie']
content _ resp.r..
resp.c..
print (cookies, content)