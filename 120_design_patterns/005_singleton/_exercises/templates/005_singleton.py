# # ---------- Singletone ----------
# 
# 
# # Real Singleton instance
# c_ Singleton o..
#     ___  -n ty__
#         __ no. '_the_instance' __ ty__. -d 
#             ty__._? _ object. -n ty__
#         r_ ty__._?
# 
# a = ?
# a.toto = 12
# 
# b = ?
# print(b.toto)
# print(id(a), id(b))  # The same !!
# 
# 
# # ---------- Borg's singletone ----------
# c_ Borg
#     __shared_state    # dict
# 
#     ___ -
#         . -d  = .__?
# 
# a = ?
# a.toto = 12
# 
# b = ?
# print(b.toto)
# print(id(a), id(b))  # different ! but states are sames
# 
# # ---------- Alex's Martelli examples ----------
# 
# c_ Singleton o..
#     ___  -n ___ $ $$
#         __ no. h.. ___ '_inst'
#             ___._? _ s___ S.. ___
# ). -n ___ $ $$
#         r_ ___._inst
# 
# c_ Borg o..
#     """Subclassing is no problem."""
#     _shared_state    # dict
#     ___  -n ___ $  $$
#         obj = s___ B.. ___. -n ___ $ $$
#         ?. -d  _ ___._?
#         r_ ?
