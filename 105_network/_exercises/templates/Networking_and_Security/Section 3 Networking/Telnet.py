______ t_l_, getp__s

# user = getpass.getuser()
user _ "ric"
pw _ getp__s.getp__s
host _ "172.30.42.127"

t _ t_l_.Telnet(host)

___
    t.read_until("login: ")
    t.w..(user + '\n')
    t.read_until("Password: ")
    t.w..(pw + '\n')

    t.read_until("~ $ ")
    t.w..("ls\n")
    print(t.read_until("~ $ "))
______ E.. __ e:
    print(e)
f..
    t.c..
