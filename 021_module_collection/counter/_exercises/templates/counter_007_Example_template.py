# # Let's assume you are working for a company that produces different kinds of widgets.
# # You are asked to identify the top 3 best selling widgets.
# # You have two separate data sources - one data source can give you a history of all widget orders
# # (widget name, quantity), while another data source can give you a history of widget refunds
# # (widget name, quantity refunded).
# # From these two data sources, you need to determine the top selling widgets (taking refinds into account of course).
# # et's simulate both of these lists:
# #
# ______ ra__
# f.. c... _______ d..d.., C..
#
# ra__.se.. 0
# widgets _ 'battery' 'charger' 'cable' 'case' 'keyboard' 'mouse'
# orders _ ra__.ch__ wi.. ra__.r..i.. 1, 5 ___ _ i_ ra.. 100
# refunds _ ra__.ch__ wi.. ra__.r..i.. 1, 3 ___ _ i_ ra.. 20)
#
# print or..
# print re..
#
# # Let's first load these up into counter objects.
# # To do this we're going to iterate through the various lists and update our counters:
#
# sold_counter _ C..
# refund_counter _ C..
#
# ___ order i_ orders
#     so.._c.. or.. 0 +_ or.. 1
#
#
# ___ refund i_ refunds
#     re.._c.. re.. 0 +_ re.. 1
#
# print(sold_counter
# # Counter({'case': 41,
# #          'battery': 61,
# #          'keyboard': 65,
# #          'cable': 39,
# #          'mouse': 46,
# #          'charger': 35})
#
# print(refund_counter
# # Counter({'battery': 7,
# #          'charger': 5,
# #          'cable': 9,
# #          'keyboard': 7,
# #          'mouse': 7,
# #          'case': 5})
#
# net_counter _ s.._c.. - re.._c..
#
# n.._c..
# # Counter({'case': 36,
# #          'battery': 54,
# #          'keyboard': 58,
# #          'cable': 30,
# #          'mouse': 39,
# #          'charger': 30})
#
# n.._c...m.._c.. 3
# # [('keyboard', 58), ('battery', 54), ('mouse', 39)]
#
# # We could actually do this a little differently, not using loops to populate our initial counters.
# # Recall the repeat() function i_ itertools:
#
# f__ it..t.. ______ re..
#
# li.. re.. 'battery' 5
# # ['battery', 'battery', 'battery', 'battery', 'battery']
#
# orders 0
# # ('case', 4)
#
# li.. re.. 0or.. 0
# # ['case', 'case', 'case', 'case']
#
# # So we could use the repeat() method to essentially repeat each widget ___ each item of orders.
# # We need to chain this up ___ each element of orders - this will give us a single iterable that we can then use
# # i_ the constructor ___ a Counter object. We can do this using a generator expression ___ example:
#
# f___ it.. ______ ch..
# print li.. ch__.fr.._it.. re.. 0or.. ___ order i_ or..
#
# order_counter _ C.. ch_.fr.._it.. re.. 0or.. ___ or.. i_ or..
#
# print or.._c..
#
# # Counter({'case': 41,
# #          'battery': 61,
# #          'keyboard': 65,
# #          'cable': 39,
# #          'mouse': 46,
# #          'charger': 35})
#
# #### Alternate Solution not using Counter
# # What if we don't want to use a Counter object. We can still do it (relatively easily) as follows:
#
# net_sales _ ||
# ___ order i_ orders
#     key _ or.. 0
#     cnt _ or.. 1
#     n.._sa.. ke. _ n._s__.ge. ke.  0 + cn.
#
# ___ refund i_ refunds
#     key _ re.. 0
#     cnt _ re.. 1
#     n.._s.. ke. _ n._s__.ge. ke. 0 - cn.
#
# # eliminate non-positive values (to mimic what - does ___ Counters)
# net_sales _  k v ___ k; v i_ n.._s__.it.. i_ v > 0
#
# # we now have to sort the dictionary
# # this means sorting the keys based on the values
# sorted_net_sales _ so.. n.._s___.it.. key_l_____ t; t 1 rev.._T..
#
# # Top three
# s.._n.._s.. :3
#
# # [('keyboard', 58), ('battery', 54), ('mouse', 39)]