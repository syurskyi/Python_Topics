# # Propagating Exceptions with raise
# ___
#     r... I...( spam # Exceptions remember arguments
# ______ I...
#     print('propagating')
#     r... # Reraise most recent exception
#
# # propagating
# # Traceback (most recent call last):
# # File "<stdin>", line 2, in <module>
# # IndexError: spam