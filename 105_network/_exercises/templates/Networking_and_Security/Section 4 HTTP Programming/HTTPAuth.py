_____ h_l_
______ b__e64
______ string

h _ "172.30.42.127"
u _ "ric"
p _ "P4ssw0rd"

authToken _ b__e64.encodestring('@:@'  (u, p)).r..('\n', '')
print(authToken)

req _ h_l_.H..(h)
req.p_r_("GET", "/protected/index.html")
req.p_h_("Host", h)
req.p_h_("Authorization", "Basic @"  authToken)
req.e_h_
req.s..("")

statusCode, statusMsg, headers _ req.g_r..
print("Response: ", statusMsg)
