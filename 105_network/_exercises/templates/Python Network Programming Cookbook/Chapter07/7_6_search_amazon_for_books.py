#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 7
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
# Supply the Amazon Access and Secret Keys via local_settings.py

______ a_p..
______ bottlenose
____ xml.dom ______ minidom __ xml

___
    ____ local_settings ______ amazon_account
______ ImportError:
    p..

ACCESS_KEY _ amazon_account['access_key'] 
SECRET_KEY _ amazon_account['secret_key'] 
AFFILIATE_ID _ amazon_account['affiliate_id'] 


___ search_for_books(tag, index):
    """Search Amazon for Books """
    amazon _ bottlenose.Amazon(ACCESS_KEY, SECRET_KEY, AFFILIATE_ID)
    results _ amazon.ItemSearch(
                SearchIndex _ index,
                Sort _ "relevancerank",
                Keywords _ tag
                )
    parsed_result _ xml.parseString(results)

    all_items _ []
    attrs _ ['Title','Author', 'URL']

    ___ item __ parsed_result.getElementsByTagName('Item'):
        parse_item _ {}

        ___ attr __ attrs:
            parse_item[attr] _ ""
            ___
                parse_item[attr] _ item.getElementsByTagName(attr)[0].childNodes[0].data
            ______:
                p..
        all_items.ap..(parse_item)
    r_ all_items

__ _______ __ ______
    parser _ ?.AP..(d.._'Search info from Amazon')
    parser.a_a..('--tag', a.._"store", d.._"tag", default_'Python')
    parser.a_a..('--index', a.._"store", d.._"index", default_'Books')
    # parse arguments
    given_args _ parser.parse_args()
    books _ search_for_books(given_args.tag, given_args.index)    
    
    ___ book __ books:
        ___ k,v __ book.iteritems
            print ("@: @" (k,v))
        print ("-" * 80)
