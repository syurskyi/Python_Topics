"""
A quick Bite to practice some string parsing extracting a users dict from a password file.

Complete get_users is how it works:

{'postfix': 'unknown', 'ssh-rsa': 'unknown', 'artagnon': 'Ramkumar R Git GSOC'}
So keys are usernames, values are names. Note that commas inside the name 
get replace by a single space. Trailing commas (not in this example) get stripped off.

Have fun and keep calm and code in Python!
"""
____ typing _______ Dict

pw = "\nmysql:x:106:107:MySQL Server,,,:/var/lib/mysql:/bin/false\navar:x:1000:1000::/home/avar:/bin/bash\nchad:x:1001:1001::/home/chad:/bin/bash\ngit-svn-mirror:x:1002:1002:Git mirror,,,:/home/git-svn-mirror:/bin/bash\ngerrit2:x:1003:1003:Gerrit User,,,:/home/gerrit2:/bin/bash\navahi:x:107:108:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false\npostfix:x:108:112::/var/spool/postfix:/bin/false\nssh-rsa:x:1004:1004::/home/ssh-rsa:/bin/bash\nartagnon:x:1005:1005:Ramkumar R,,,,Git GSOC:/home/artagnon:/bin/bash\n"
_______ __

___ get_users_1st_solution(passwd: s..) __ d..:

    result    # dict
    passwd = passwd.strip('\n')
    lines = passwd.s..('\n')
    ___ line __ lines:
        fields = line.s..(':')
        k = fields[0]
        v = fields[4]
        __ v __ "":
            v = "unknown"
        ____:
            v = __.sub(',+', ' ', v)
            v = v.s..
        result[k] = v
    r..(result)

___ get_users_2nd_solution(passwd: s..) __ d..:

    output    # dict
    ___ row __ passwd.s...splitlines
        fields = row.s..(':')
        username = fields[0]
        name = __.sub(r',+', r' ', fields[4].strip(',')) o. 'unknown'
        output[username] = name
    r.. output

print(get_users(pw))
