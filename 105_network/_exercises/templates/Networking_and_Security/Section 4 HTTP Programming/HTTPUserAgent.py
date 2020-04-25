______ h_l_

h _ "www.infiniteskills.com"

req _ h_l_.H..(h)
req.p_r_("GET", "/")
req.p_h_("Host", h)
req.p_h_("User-Agent", "Garbage browser: 5.6")
req.p_h_("My-Header", "My value")
req.e_h_
req.s..("")

statusCode, statusMsg, headers _ req.g_r..
print("Response: ", statusMsg)

