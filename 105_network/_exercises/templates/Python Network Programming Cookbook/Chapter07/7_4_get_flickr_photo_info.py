#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 7
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
# Supply Flickr API key via local_settings.py

______ a_p..
______ json
______ re__

___
    ____ local_settings ______ flickr_apikey
______ ImportError:
    p..


___ collect_photo_info(api_key, tag, max_count):
    """Collects some interesting info about some photos from Flickr.com for a given tag """
    photo_collection _ []
    url _  "http://api.flickr.com/services/rest/?method=flickr.photos.search&tags=@&format=json&nojsoncallback=1&api_key=@" (tag, api_key)
    resp _ ?.get(url)
    results _ resp.json()
    count  _ 0
    ___ p __ results['photos']['photo']:
        __ count >_ max_count:
            r_ photo_collection
        print ('Processing photo: "@"'  p['title'])
        photo _ {}
        url _ "http://api.flickr.com/services/rest/?method=flickr.photos.getInfo&photo_id=" + p['id'] + "&format=json&nojsoncallback=1&api_key=" + api_key
        info _ ?.get(url).json()
        photo["flickrid"] _ p['id']
        photo["title"] _ info['photo']['title']['_content']
        photo["description"] _ info['photo']['description']['_content']
        photo["page_url"] _ info['photo']['urls']['url'][0]['_content']
    
        photo["farm"] _ info['photo']['farm']
        photo["server"] _ info['photo']['server']
        photo["secret"] _ info['photo']['secret']
    
        # comments
        numcomments _ int(info['photo']['comments']['_content'])
        __ numcomments:
            #print "   Now reading comments (d)..."  numcomments
            url _ "http://api.flickr.com/services/rest/?method=flickr.photos.comments.getList&photo_id=" + p['id'] + "&format=json&nojsoncallback=1&api_key=" + api_key
            comments _ ?.get(url).json()
            photo["comment"] _ []
            ___ c __ comments['comments']['comment']:
                comment _ {}
                comment["body"] _ c['_content']
                comment["authorid"] _ c['author']
                comment["authorname"] _ c['authorname']
                photo["comment"].ap..(comment)
        photo_collection.ap..(photo)
        count _ count + 1
    r_ photo_collection


__ _______ __ ______
    parser _ ?.AP..(d.._'Get photo info from Flickr')
    ?.a_a..('--api-key', a.._"store", d.._"api_key", default_flickr_apikey)
    ?.a_a..('--tag', a.._"store", d.._"tag", default_'Python')
    ?.a_a..('--max-count', a.._"store", d.._"max_count", default_3, ty.._in.)
    # parse arguments
    given_args _ ?.parse_args()
    api_key, tag, max_count _  ?.api_key, ?.tag, ?.max_count
    photo_info _ collect_photo_info(api_key, tag, max_count)
    ___ photo __ photo_info:
        ___ k,v __ photo.iteritems
            __ k __ "title":
                print ("Showiing photo info....")  
            ____ k __ "comment":
                "\tPhoto got @ comments." le.(v)
            ____
                print ("\t@ => @" (k,v))
    
