# # Propagating Exceptions with raise
# t__
#     r... I...( spam # Exceptions remember arguments
# e_____ I...
#     print('propagating')
#     r... # Reraise most recent exception
#
# # propagating
# # Traceback (most recent call last):
# # File "<stdin>", line 2, in <module>
# # IndexError: spam