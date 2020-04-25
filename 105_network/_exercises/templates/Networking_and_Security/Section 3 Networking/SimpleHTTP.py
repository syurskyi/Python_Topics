______ http.client

h _ http.client.H..Connection("www.infiniteskills.com")
h.request("GET", "/")
data _ h.getresponse
print (data.code)
print (data.headers)
text _ data.r_l..
___ t __ text:
    print(t.d..('utf-8'))

