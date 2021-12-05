# ____ ____
# ____ t___
#
# ____ aiohttp
#
#
# c_ Photo
#     ___  -   album_id photo_id title url thumbnail_url
#         thumbnailUrl = ?
#         ? = ?
#         ? = ?
#         ? = ?
#         albumId = ?
#
#     $$
#     ___ from_json ___ ___
#         r_ Photo ___ albumId ___ id ___ title ___ url ___ thumbnailUrl
#
#
# ___ print_photo_titles photos
#     ___ photo __ ?
#         print _* ?.t.. e.._'\n'
#
#
# _____ ___ photos_by_album task_name, album, session
#     print _* |t..=
#     url = _ * https://jsonplaceholder.typicode.com/albums/{album}/photos/
#     response = _____ s___.g.. ?
#     photos_json = _____ ?.j..
#
#     _____ ____.s.. 1
#     r_ ?.f.... p.. ___ photo __ p..
#
#
# _____ ___ download_albums albums
#     _____ w___ a___.C.. __ session
#         ___ album __ ?
#             __ n.. isi.. ? in.
#                 r__ R.... invalid album number
#             _____ _____ p.. _* t|?| a.. s..
#
#
# _____ ___ main
#     ___
#         _____ ___ photos __ d.. 1, 2, 'a', 4
#             p... ?
#     _______ E... __ ex
#         print re__ ?
#
#
# __ _______ __ _______
#     ____.r.. m..
#
#     t___.s.. 3
#     print('main ended')
