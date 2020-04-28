import httplib

host = "172.30.42.126"

req = httplib.HTTP(host)
req.putrequest("HEAD", "/")
req.putheader("Host", host)
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Status: ", statusCode)
