import u__.r..

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"

req = u__.r...Request("https://www.python.org", headers=headers)
html = u__.r...urlopen(req).read()
print(html.decode())

print("\n\nDownloading Wordpress...")
rsp = u__.r...urlopen("https://wordpress.org/latest.zip")
data = rsp.read()

filename = "latest.zip"
file_ = open(filename, "wb")
file_.write(data)
file_.close()
print("Download Complete")