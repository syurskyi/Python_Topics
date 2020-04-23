# ch11/example4.py

______ ai..
______ a..

? ___ get_html(session, url):
    ? w__ session.g..(url, ssl_F..) as res:
        r_ await res.text()

? ___ main():
    ? w__ ?.ClientSession() as session:
        html _ await get_html(session, 'http://packtpub.com')
        print(html)

loop _ ?.g_e_l..
loop.r_u_c..(main())
