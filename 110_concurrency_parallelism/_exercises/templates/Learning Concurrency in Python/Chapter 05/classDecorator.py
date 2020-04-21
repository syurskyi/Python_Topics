# ____ t.. ______ L...
#
# ___ lock_class methodnames lockfactory
#     r_ l___ cls m_t..|? m.. l..
#
# ___ lock_method method
#     __ g_a.. ? '__is_locked' F..
#         r_ T.. "Method @ is already locked!"  ?
#     ___ l.. $ $$
#         w__ _lock
#             r_ m.. $ $$
#     l__. -n _ '@(@)'  ('lock_method' ?. -n
#     l__.__is_locked _ T..
#     r_ ?
#
#
# ___ make_threadsafe cls methodnames lockfactory
#     init _ ?. -
#     ___ newinit $ $$
#         i.. $ $$
#         ._lock _ l..
#     ___. - _ n..
#
#     ___ methodname __ ?s
#         oldmethod _ g_a.. ___ ?
#         newmethod _ l.. ?
#         s_a.. ___ m.. n..
#
#     r_ ___
#
#
# ?? 'add','remove'|, L..
# c_ ClassDecoratorLockedSet se.
#
#     @lock_method # __ you double-lock a method, a TypeError is raised
#     ___ lockedMethod
#         print("This section of our code would be thread safe")
#         p..
