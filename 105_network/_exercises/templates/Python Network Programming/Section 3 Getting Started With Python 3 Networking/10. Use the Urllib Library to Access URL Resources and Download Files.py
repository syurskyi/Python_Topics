______ u_l_.request

headers _   # dict
headers['User-Agent'] _ "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

req _ u_l_.request.R..("https://www.python.org", headers_headers)
html _ u_l_.request.u_o..(req).r..
print(html.d..)

print("\n\nDownloading Wordpress...")
rsp _ u_l_.request.u_o..("https://wordpress.org/latest.zip")
data _ rsp.r..

filename _ "latest.zip"
file_ _ o..(filename, __)
file_.w..(data)
file_.c..
print("Download Complete")