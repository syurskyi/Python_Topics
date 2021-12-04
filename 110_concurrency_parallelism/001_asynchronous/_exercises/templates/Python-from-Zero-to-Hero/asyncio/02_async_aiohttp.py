# ____ ____
#
# ____ aiohttp __ aiohttp
#
# _____ m__.d.. ____ a..
#
#
# c_ Photo
#     ___  -   album_id photo_id title url thumbnail_url
#         ? = ?
#         ? = ?
#         ? = ?
#         ? = ?
#         ? = ?
#
#     $$
#     ___ from_json ___ ___
#         r_ ? obj['albumId' obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])
#
#
# ___ print_photo_titles photos
#     ___ photo __ ?
#         print _* ?.t.., e.._'\n'
#
#
# _____ ___ photos_by_album task_name, album, session
#     print _* t.. =
#     url = f'https://jsonplaceholder.typicode.com/photos?albumId= a..
#
#     response = _____ s__.g.. ?
#     photos_json = _____ ?.j..
#
#     r_ ?.f.. p.. ___ ? __ ?
#
#
# @a..
# _____ ___ main
#
#     _____ w___ a__.C.. __ session:
#         photos_in_albums = _____ ____.g.. * p.. _*Task {i + 1}', a.. s..
#                                                   ___ i, a.. __ e___ r__ 2, 30
#
#         photos_count = s__ l__(cur) ___ ? __ p..
#         print _* photos_count=
#
#
# __ _______ __ _______
#
#     loop = ____.g..
#     ___
#         ?.c.. m..
#         ?.r..
#     _______
#         ?.c..
