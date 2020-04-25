______ h_l_

host _ "172.30.42.126"

req _ h_l_.H..(host)
req.p_r_("HEAD", "/")
req.p_h_("Host", host)
req.e_h_
req.s..("")

statusCode, statusMsg, headers _ req.g_r..
print("Status: ", statusCode)
