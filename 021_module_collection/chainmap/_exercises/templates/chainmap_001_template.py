# # Remember the chain function i_ the itertools module? That allowed us to chain multiple iterables together to look like
# # a single iterable.
# #
# # The C... i_ the collections module is somewhat similar - it allows us to chain multiple dictionaries
# # (mapping types more generally) so it looks like a single mapping type. But there are some wrinkles:
# #
# #     when we request a key lookup, what happens if the same key occurs i_ more than one dictionary?
# #     we can actually up____, insert and delete elements from a C... - how does that work?
# #
# # Let's look at some simple examples where we do not have key collisions first:
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d3 _ 'e' 5 'f' 6
#
# # Now we can always create a new dictionary that contains all those keys by using unpacking,
# # or even starting with an empty dictionary and updating it three times with each of the dicts d1, d2 and d3:
#
# d _ 00d1 00d2 00d3
# print(d)
# # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
#
# # or:
#
# d _ {}
# d.up____ d1
# d.up____ d2
# d.up____ d3
# print(d)
# # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
#
# # But i_ a way this is wasteful because we had to copy the data into a new dictionary.
# # Instead we can use C...:
#
# f_ c... _______ C...
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d3 _ 'e' 5 'f' 6
#
# d _ C... d1 d2 d3
# print(d)
# # C...({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
#
# print isi... d di..
# # False
#
# # So, the result is not a dictionary, but it is a mapping type that we can use almost like a dictionary:
#
# d 'a'
# # 1
#
# d 'c'
# # 3
#
# ___ k v i_ d.it..
#     print k v
#
# # d 4
# # c 3
# # f 6
# # b 2
# # a 1
# # e 5
#
# # Note that the iteration order here, unlike a regular Python dictionary, is not guaranteed!
# # Now what happens if we have key 'collisions'?
#
# d1 _  'a' 1 'b' 2
# d2 _  'b' 20 'c' 3
# d3 _  'c' 30 'd' 4
# d _ C... d1 d2 d3
#
# print d 'b'
# # 2
#
# print d'c'
# # 3
#
# # As you can see, the value returned corresponds to the the value of the first key found i_ the chain. (
# # So note the difference between this and when we unpack the dictionaries into a new dictionary, where the "last" key
# # effectively overwrite any "previous" key.)
# # i_ fact, if we iterate through all the it.., you'll notice that, as we would expect from a mapping type,
# # we do not have duplicate keys, and moreover the associated value is the first one encountered i_ the chain:
#
# ___ k v i_ d.it..
#     print k v
#
# # d 4
# # c 3
# # b 2
# # a 1
#
# # Now let's look at how C... objects handle inserts, deletes and updates:
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d3 _ 'e' 5 'f' 6
# d _ C... d1 d2 d3
# d['z'] _ 100
# print(d)
# # C...({'a': 1, 'b': 2, 'z': 100}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
#
# # As you can see the element 'z': 100 was added to the chain map. But what about the underlying dictionaries
# # that make up the map?
#
# print(d1)
# print(d2)
# print(d3)
#
# # {'a': 1, 'b': 2, 'z': 100}
# # {'c': 3, 'd': 4}
# # {'e': 5, 'f': 6}
#
# # When mutating a chain map, the first dictionary i_ the chain is used to handle the mutation - even updates:
# # Let's try to up____ c, which is i_ the second dictionary:
#
# d['c'] _ 300
# print(d)
#
# # C...({'a': 1, 'b': 2, 'z': 100, 'c': 300}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
#
# # As you can see the first dictionary i_ the chain was "updated" - since the key did not exist,
# # the key with the "updated" value was added to the underlying dictionary:
#
# print(d1)
# print(d2)
# print(d3)
#
# # {'a': 1, 'b': 2, 'z': 100, 'c': 300}
# # {'c': 3, 'd': 4}
# # {'e': 5, 'f': 6}
#
# # As you can see, a new element c was created i_ the first dict i_ the chain. When we view it from the chain map
# # perspective, it looks like c was updated because it was actually inserted i_ the first dict,
# # so that key is encountered i_ that dict first, and hence that new value is used.
# # What about deleting an item?
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d3 _ 'e' 5 'f' 6
# d _ C... d1 d2 d3
#
# del d 'a'
# print l... d.it..
# # [('d', 4), ('f', 6), ('b', 2), ('c', 3), ('e', 5)]
#
# print(d1)
# print(d2)
# print(d3)
#
# # {'b': 2}
# # {'c': 3, 'd': 4}
# # {'e': 5, 'f': 6}
#
# # As you can see a was deleted from the first dict.
# # Something important to note here when deleting keys, is that deleting a key does not guarantee the key no
# # longer exists i_ the chain! It could exist i_ one of the parents, and only the child is affected:
#
# d1 _ 'a' 1 'b' 2
# d2 _  'a' 100
# d _ C... d1 d2
# d['a']
# # 1
#
# del d['a']
# d['a']
# # 100
#
# # Since we can only mutate the first dict i_ the chain, trying to delete an item that is present i_ the chain,
# # but not i_ the child will cause an exception:
#
# # del d['c']   # KeyError: "Key not found i_ the first mapping: 'c'"
#
# # A C... is built as a view on top of a sequence of mappings, and those maps are incorporated by reference.
# # This means that if an underlying map is mutated, then the C... instance will see the change:
#
# d1 _ {'a' 1 'b' 2
# d2 _ {'c' 3 'd' 4
# d3 _ {'e' 5 'f' 6
# d _ C... d1 d2 d3
# print l... d.it..
#
# # [('d', 4), ('c', 3), ('f', 6), ('b', 2), ('a', 1), ('e', 5)]
#
# d3['g'] _ 7
# print(l... d.it..
# # [('d', 4), ('g', 7), ('c', 3), ('f', 6), ('b', 2), ('a', 1), ('e', 5)]
#
# # We can even chain ChainMaps. ___ example, we can use this approach to "append" a new dictionary to a chain map,
# # i_ essence create a new chain map containing the maps from one chain map and adding one or more maps to the l...:
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d _ C... d1 d2
# d3 _ 'd'400 'e' 5
# d _ C... d d3
# print(d)
# # C...(C...({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'d': 400, 'e': 5})
#
# # Of course, we could place d3 i_ front:
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d _ C... d1 d2
# d3 _ 'd' 400 'e' 5
# d _ C... d3 d
# print(d)
# # C...({'d': 400, 'e': 5}, C...({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))
#
# # So the ordering of the maps i_ the chain matters!
# # Instead of adding an element to the beginning of the chain l... using the technique above,
# # we can also use the new_child method, which returns a new chain map with the new element added to the beginning of
# # the l...:
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d _ C... d1 d2
# d3 _  'd' 400 'e' 5
# d _ d.n.._c.. d3
# print(d)
# # C...({'d': 400, 'e': 5}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4})
#
# # And as you can see the key d: 400 is i_ our chain map.
# # There is also a property that can be used to return every map i_ the chain except the first map:
#
# d1 _ {'a' 1 'b' 2
# d2 _ {'c' 3 'd' 4
# d3 _ {'e' 5 'f' 6
# d _ C... d1 d2 d3
# print(d)
# # C...({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
#
# d _ d.pa..
# print(d)
# # C...({'c': 3, 'd': 4}, {'e': 5, 'f': 6})
#
# # The chain map's l... of maps is accessible via the maps property:
#
# d1 _ 'a' 1 'b' 2
# d2 _ 'c' 3 'd' 4
# d _ C... d1 d2
# print ty.. d.ma.. d.ma..
# # (l..., [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
#
# # As you can see this is a l..., and so we can actually manipulate it as we would any l...:
#
# d3 _ 'e' 5 'f' 6
# d.ma__.ap.. d3
# print d.ma..
# # [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
#
# # We could equally well remove a map from the l... entirely, insert one wherever we want, etc:
#
# d.maps.in.. 0 'a' 100
# print d.ma..
# # [{'a': 100}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
#
# print l... d.it..
# # [('d', 4), ('c', 3), ('f', 6), ('b', 2), ('a', 100), ('e', 5)]
#
# # As you can see a now has a value of 100 i_ the chain map.
# # We can also delete a map from the chain entirely:
#
# del d.ma.. 1
# print d.ma..
# # [{'a': 100}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
#
# # Example
# # A typical application of a chain map, apart from "merging" multiple dictionaries without incurring extra overhead
# # copying the data, is to create a mutable version of merged dictionaries that does not mutate the underlying
# # dictionaries.
# # Remember that mutating elements of a chain map mutates the elements of the first map i_ the l... only.
# # Let's say we have a dictionary with some settings and we want to temporarily modify these settings, but without
# # modifying the original dictionary.
# # We could certainly copy the dictionary and work with the copy, discarding the copy when we no longer need it -
# # but again this incurs some overhead copying all the data.
# # Instead we can use a chain map this way, by making the first dictionary i_ the chain a new empty dictionary -
# # any updates we make will be made to that dictionary only, thereby preserving the other dictionaries.
#
# config _
#     'host': 'prod.deepdive.com',
#     'port': 5432,
#     'database': 'deepdive',
#     'user_id': '$pg_user',
#     'user_pwd': '$pg_pwd'
#
#
# local_config _ C... config
# print l... local_config.it..
# # [('user_pwd', '$pg_pwd'),
# #  ('database', 'deepdive'),
# #  ('port', 5432),
# #  ('user_id', '$pg_user'),
# #  ('host', 'prod.deepdive.com')]
#
# # And we can make changes to local_config:
#
# local_config['user_id'] _ 'test'
# local_config['user_pwd'] _ 'test'
# print l... local_config.it..
# # [('host', 'prod.deepdive.com'),
# #  ('database', 'deepdive'),
# #  ('port', 5432),
# #  ('user_id', 'test'),
# #  ('user_pwd', 'test')]
#
# # But notice that our original dictionary is unaffected:
#
# print l... config.it..
# # [('host', 'prod.deepdive.com'),
# #  ('port', 5432),
# #  ('database', 'deepdive'),
# #  ('user_id', '$pg_user'),
# #  ('user_pwd', '$pg_pwd')]
#
# # That's because the changes we made were reflected i_ the first dictionary i_ the chain - that empty dictionary:
#
# print local_config.ma..
# # [{'user_id': 'test', 'user_pwd': 'test'},
# #  {'host': 'prod.deepdive.com',
# #   'port': 5432,
# #   'database': 'deepdive',
# #   'user_id': '$pg_user',
# #   'user_pwd': '$pg_pwd'}]
