# #!/usr/bin/env python
# # Python Network Programming Cookbook, Second Edition -- Chapter - 7
# # This program is optimized for Python 2.7.12 and Python 3.5.2.
# # It may run on any other version with/without modifications.
# # Supply Flickr API key via local_settings.py
#
# ______ a_p..
# ______ j..
# ______ re__
#
# ___
#     ____ local_settings ______ f_a..
# ______ I..
#     p..
#
#
# ___ collect_photo_info api_key  tag  max_count
#     """Collects some interesting info about some photos from Flickr.com for a given tag """
#     photo_collection _ # list
#     url _  "http://api.flickr.com/services/rest/?method=flickr.photos.search&tags=@&format=json&nojsoncallback=1&api_key=@" (tag, api_key)
#     resp _ ?.g.. ?
#     results _ resp.?
#     count  _ 0
#     ___ p __ r.. 'photos' 'photo'
#         __ c.. >_ m_c..
#             r_ p_c..
#         print ('Processing photo: "@"'  p 'title'
#         photo _   # dict
#         url _ "http://api.flickr.com/services/rest/?method=flickr.photos.getInfo&photo_id=" + p['id'] + "&format=json&nojsoncallback=1&api_key=" + api_key
#         info _ ?.g.. ? .?
#         ? "flickrid" _ p 'id'
#         ? "title" _ i.. 'photo' 'title' '_content'
#         ? "description" _ i.. 'photo' 'description' '_content'
#         ? "page_url"] _ i..'photo' 'urls' 'url' 0 '_content'
#
#         ? "farm"] _ i.. 'photo' 'farm'
#         ? "server"] _ i..'photo' 'server'
#         ? "secret"] _ i..'photo' 'secret'
#
#         # comments
#         numcomments _ in. i..'photo' 'comments' '_content'
#         __ ?
#             #print "   Now reading comments (d)..."  numcomments
#             url _ "http://api.flickr.com/services/rest/?method=flickr.photos.comments.getList&photo_id=" + p['id'] + "&format=json&nojsoncallback=1&api_key=" + a_k..
#             comments _ ?.g.. ? . ?
#             ? "comment" _  # list
#             ___ c __ ? 'comments' 'comment'
#                 comment _ # dict
#                 ?["body"] _ c['_content']
#                 ?["authorid"] _ c['author']
#                 ?["authorname"] _ c['authorname']
#                 ?["comment"].ap.. c..
#         p_c__.ap.. p..
#         count _ c.. + 1
#     r_ ?
#
#
# __ _______ __ ______
#     parser _ ?.AP.. d.._'Get photo info from Flickr'
#     ?.a_a.. '--api-key' a.._"store"  d.._"api_key"  d.._f_a..
#     ?.a_a.. '--tag'  a.._"store"  d.._"tag"  d.._'Python'
#     ?.a_a.. '--max-count'  a.._"store"  d.._"max_count"  d.._3  ty.._in.
#     # parse arguments
#     given_args _ ?.p_a..
#     api_key  tag  max_count _  ?.?  ?.?  ?.?
#     photo_info _ c_p_i.. a_k.. t.. m_c..
#     ___ photo __ ?
#         ___ k v __ ?.i_i..
#             __ k __ "title"
#                 print ("Showiing photo info....")
#             ____ k __ "comment"
#                 "\tPhoto got @ comments." le. v
#             ____
#                 print ("\t@ => @"  k v
#
