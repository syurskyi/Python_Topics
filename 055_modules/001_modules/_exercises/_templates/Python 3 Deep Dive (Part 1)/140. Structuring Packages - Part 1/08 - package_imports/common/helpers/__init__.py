# # helpers
#
# ____ .c... ________ C..
#
#
# # I don't consider the following good style:
# # It works, but it might be unexpected for most users.
# # They might not even think that the __init__ file
# # would contain functional code, so they might be left wondering
# # where say_hello and factorial actually came from!
#
# ___ say_hello name
#     r_ _*Hello ?'
#
#
# ___ factorial n
#     __ n <_ 1
#         r_ 1
#     ____
#         r_ n * ? ?-1
