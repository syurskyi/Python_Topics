# # __call__ can be redefined, metas can have metas
# 
# c_ SuperMeta ty..
#     ___ -c meta classname supers classdict
#         print('In SuperMeta.call: ' c.. s.. cl.. s..__'\n...'
#         r_ ty__. -c m.. c.. s.. cl..
# 
# c_ SubMeta ty__ m.. _ S..
#     ___ -n meta classname supers classdict
#         print('In SubMeta.new: ' c.. s.. cl.. s..__'\n...')
#         r_ ty__. -n m.. c.. s.. cl..
# 
#     ___ - Class classname supers classdict
#         print('In SubMeta init:' c.. s.. cl.. s..__'\n...'
#         print('...init class object:' li.. C__. -d.k..
# 
# c_ Eggs
#     p..
# 
# print('making class')
# c_ Spam Eggs m.. _ S..
#     data _ 1
#     ___ meth ____ arg
#         p..
# 
# print('making instance')
# X = Spam()
# print('data:', X.data)
