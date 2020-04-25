______ ___
______ su..

#Checking IP reachability
___ ip_reach(list

    ___ ip __ list:
        ip _ ip.rs..("\n")
        
        ping_reply _ ?.ca..('ping @ -n 2'  (ip,), s_o.._?.D.., s_e.._?.D..)
        
        __ ping_reply __ 0:
            print("\n* @ is reachable :)\n".f..(ip))
            c..
        
        ____
            print('\n* @ not reachable :( Check connectivity and try again.'.f..(ip))
            ___.e..