______ so..
______ __

sock _ ?.?(?.A.. ?.S..
sock.c..(("www.microsoft.com", 80))

http_get _ b"GET / HTTP/1.1\nHost: www.microsoft.com\n\n"
data _ ''
___
    sock.s_a..(http_get)
    data _ sock.r_f..(1024)
______ ?.e..
    print ("Socket error", ?.er..
f..
    print("closing connection")
    sock.c..

strdata _ data[0].d..("utf-8")
#  looks like one long line so split it at newline into multiple strings
headers _ strdata.s_l..
#  use regular expression library to look for the one line we like
___ s __ headers:
    __ __.s..('Server:', s
        s _ s.r..("Server: ", "")
        print(s)
