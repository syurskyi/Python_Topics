# ______ __ re.. ___ a_p_
#
#
# c_ RegEx
#     ___  -  pattern desc
#         ? ?
#         ?
#
#
# rgxEmail _ ? _"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", "Emails")
# rgxPhone _ ? _"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", "Phone Numbers")
# rgxIP _ ? _"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP Addresses")
# rgxWor. _ ? _"[a-zA-Z]+", "Words")
#
#
# ___ scrapeURL url rgx
#     ___
#         src _ r__.g.. ?.st..
#         ___ rg __ ?
#             print("[*] Scraping" + ?.d.. + " form " + ?.st..
#             res _ set(__.f_a.. ?.p.. s__.t.. __.I
#             ___ dat __ ?
#                 print ?
#     ______ E.. __ err
#         print st. ?
#
#
# ___ scrapeFile fle rgx
#     ___
#         w__ o.. ? __ fh
#             ___ url __ ?
#                 ? ? r..
#     ______ E.. __ err
#         print st. ?
#
#
# ___ main args
#     rgx _   # list
#     isFile _ T..
#     __ ?.in__.l__.s_w.. "http"
#         isFile _ F..
#     __ ?.s__.l__ __ "e":  # scrape emails
#         rgx _ ?
#     ____ ?.s__.l__ __ "p":  # scrape phone #
#         rgx _ ?
#     ____ ?.scrape.l__ __ "w":  # scrape words
#         rgx _ ?
#     ____ ?.s__.l__ __ "i":  # scrape IP
#         rgx _ ?
#     ____ ?.s__.l__ __ "a":  # scrape everything
#         rgx _ ? ? ? ?
#
#     __ isFile
#         sF.. ?.in__ ?
#     ____
#         sU.. ?.in__ ?
#
#     print("================================================")
#
#
# __ _______ __ _______
#     parser _ a_p_.A_P..
#     ?.a_a.. "input" a.._"store" t.._st. h.._"The URL or file containing URLs to scrape")
#     ?.a_a.. "scrape" a.._"store" t.._st. n.._"?", d.._"a",
#                         h.._"e = Email, p = Phone, i = IPs, w = Words, a = All")
#
#     __ le.(___.a.. 2; __ 0
#         ?.p_h..
#         ?.e..
#
#     args _ ?.p_a..
#     main ?