# _______ s____
#
#
# ___ parse_http_response text_response
#     lines _ t.._r___.sp... *\n*
#     status_raw, lines _ l..|0| l...|1;|
#     protocol, status_code, message _ st..____.sp.. ' '
#     empty_index _ 1
#     headers _ ||  # dictionary
#     ___ index line i_ en.. li..
#         line _ l__.st..
#         line _ l___.st.. *\r*
#         i_ line __ ''
#             empty_index _ index
#             b...
#         print l...
#         k _ v _ l__.par___ *:*
#         hea___.set___ k.st__ v.st...
#     content _ **.j___ l...|e..._i... + 1;
#     r_ i00 s..._c... hea.. con...
#
#
# sock _ s______.s______(s______.AF_INET, s______.SOCK_STREAM)
# s___.c... example.com 80
# content_items _ |
#     'GET / HTTP/1.1',
#     'Host: example.com',
#     'Connection: keep-alive',
#     'Accept: text/html',
#     '\n'
# |
# content _ *\n*.j___ c..._i...
# print --- HTTP MESSAGE ---
# print c....
# print --- END OF MESSAGE ---
# s___.s... c___.e___
# result _ s___.r... 10024
# s.._c.. h.... c... _ p.... r___.d___
# print *Status Code: ||*.f... s.._c..
# print *Headers: ||*.f... h...
# print Content:
# print c...
