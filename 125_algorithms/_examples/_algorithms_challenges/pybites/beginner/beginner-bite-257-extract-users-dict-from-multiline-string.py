"""
A quick Bite to practice some string parsing extracting a users dict from a password file.

Complete get_users is how it works:

{'postfix': 'unknown', 'ssh-rsa': 'unknown', 'artagnon': 'Ramkumar R Git GSOC'}
So keys are usernames, values are names. Note that commas inside the name 
get replace by a single space. Trailing commas (not in this example) get stripped off.

Have fun and keep calm and code in Python!
"""
from typing import Dict

pw = "\nmysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false\navar:x:1000:1000::/home/avar:/bin/bash\nchad:x:1001:1001::/home/chad:/bin/bash\ngit-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash\ngerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash\navahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false\npostfix:x:108:112::/var/spool/postfix:/bin/false\nssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash\nartagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash\n"
import re

def get_users_1st_solution(passwd: str) -> dict:

    result = {}
    passwd = passwd.strip('\n')
    lines = passwd.split('\n')
    for line in lines:
        fields = line.split(':')
        k = fields[0]
        v = fields[4]
        if v == "":
            v = "unknown"
        else:
            v = re.sub(',+', ' ', v)
            v = v.strip()
        result[k] = v
    return(result)

def get_users_2nd_solution(passwd: str) -> dict:

    output = {}
    for row in passwd.strip().splitlines():
        fields = row.split(':')
        username = fields[0]
        name = re.sub(r',+', r' ', fields[4].strip(',')) or 'unknown'
        output[username] = name
    return output

print(get_users(pw))
