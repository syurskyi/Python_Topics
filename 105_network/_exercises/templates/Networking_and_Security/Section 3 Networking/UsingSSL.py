______ ssl
______ so..

s _ ?.?(?.A.. ?.S..
ssock _ ssl.wrap_socket(s)

___
    ssock.c..(("www.google.com", 443))
    print(ssock.cipher)
______:
    print("error")

___
    ssock.w..(b"GET / HTTP/1.1 \r\n")
    ssock.w..(b"Host: www.google.com\n\n")
______ E.. __ e:
    print("write error: ", e)

data _ b_a_
___
    data _ ssock.r..
______ E.. __ e:
    print("read error: ", e)

print(data.d..("utf-8"))

