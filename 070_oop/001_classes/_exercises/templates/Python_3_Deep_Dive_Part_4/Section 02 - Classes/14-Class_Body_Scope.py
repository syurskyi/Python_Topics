# # %%
# '''
# ### Class Body Scope
# '''
#
# # %%
# '''
# The class body is a scope and therefore has it's own namespace. Inside that scope we can reference symbols like
# we would within any other scope:
# '''
#
# # %%
# c_ Language
#     MAJOR _ 3
#     MINOR _ 7
#     REVISION _ 4
#     FULL _ | | | .f..mM... M... R..
#
# # %%
# print ?.F..
#
# # %%
# '''
# However, functions defined inside the class are not nested in the body scope - instead they are nested in whatever
# scope the class itself is in.
# '''
#
# # %%
# '''
# This means that we cannot reference the class symbols inside a function without also telling Python where to look for
# it:
# '''
#
# # %%
# c_ Language
#     MAJOR _ 3
#     MINOR _ 7
#     REVISION _ 4
#
#     0p...
#     ___ version ____
#         r_ | | | .f... ____.M.... ____.M.... ____.R....
#
#     0c...
#     ___ cls_version cls
#         r_ | | | .f... cl_.M...., cl_.M...., cl_.R....)
#
#     0s..
#     ___ static_version():
#         r_ | | | .f...(?.M...., ?.M...., ?.R....)
#
# # %%
# l _ ?
# print ?.v..
#
# # %%
# ?.c...
#
# # %%
# ?.s..
#
# # %%
# '''
# Basically think that the function symbols are in the class body namespace, but the functions themselves are defined
# externally to the class - just as if we had written it this way:
# '''
#
# # %%
# ___ full_version
#  r_ | | | .f... ?.M..., ?.M.... ?.R....
#
# # %%
# f...
#
# # %%
# '''
# So writing something like this will not work:
# '''
#
# # %%
# c_ Language
#     MAJOR _ 3
#     MINOR _ 7
#     REVISION _ 4
#
#     @classmethod
#     ___ cls_version cls)
#         r_ | | | .f... M.... M.... R....
#
# # %%
# ?.c..
#
# # %%
# '''
# This behavior can lead to subtle bugs if we aren't careful.
# '''
#
# # %%
# '''
# What happens if the names `MAJOR`, `MINOR` and `REVISION` **are** defined in the enclosing scope?
# '''
#
# # %%
# MAJOR _ 0
# MINOR _ 0
# REVISION _ 1
#
# # %%
# ?.c..
#
# # %%
# '''
# See what happened?!!
# '''
#
# # %%
# '''
# Now of course, the nested scopes follow the same usual rules, so we could technically have something like this:
# '''
#
# # %%
# MAJOR _ 0
# MINOR _ 0
# REVISION _ 1
#
# ___ gen_class
#     MAJOR _ 0
#     MINOR _ 4
#     REVISION _ 2
#
#     c_ Language
#         MAJOR _ 3
#         MINOR _ 7
#         REVISION _ 4
#
#         0c...
#         ___ version cls
#             r_ | | | .f... M.... M.... R....
#
#     r_ ?
#
# # %%
# cl_ _ g...
#
# # %%
# cl_.v..
#
# # %%
# '''
# Notice how the scope of `version` was nested inside `gen_class` which itself is nested in the `global` scope.
# When we called the `version` method, it found the `MAJOR`, `MINOR` and `REVISION` in the closest enclosing scope -
# which turned out to be the `gen_class` scope.
# This means by the way, that `version` is not only a method, but actually a closure.
# '''
#
# # %%
# ______ ins..
#
# # %%
# i____.g..c..v.. cl_.v..
#
# # %%
# '''
# This last example of "unexpected" behavior I want to show you was show to me by a friend who was puzzled by it:
# '''
#
# # %%
# name _ 'Guido'
#
# c_ MyClass
#     name _ 'Raymond'
#     list_1 _ |na.. * 3
#     list_2 _ |na__.up.. ___ i i_ ra.. 3
#
#     0c..
#     ___ hello cls
#         r_  | says hello .f... n..
#
# # %%
# print ?.l._1
#
# # %%
# '''
# Since the expression `[name] * 3` lives in the class body, it uses `name` that it finds in the class namespace.
# '''
#
# # %%
# ?.h..
#
# # %%
# '''
# Here, `name` is used inside a function, so the closest `name` symbol is the one in the module/global scope.
# Hence we see that `Guido` was used.
# '''
#
# # %%
# print ?.l.._2
#
# # %%
# '''
# That one is more puzzling... Why is the expression `[name.upper() for i in range(3)]` using `name` from the enclosing
# (module/global) scope, and not the one from the class namespace like `[name] * 3` did?
# '''
#
# # %%
# '''
# Remember what we discussed about comprehensions?
# '''
#
# # %%
# '''
# They are essentially thinly veiled **functions**!!!
# '''
#
# # %%
# '''
# So they behave like a function would, and therefore are not nested in the class body scope, but, in this case,
# in the module/global scope!
# '''