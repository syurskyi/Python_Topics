# # w - writes and erases existing contents
# w__ o.. haiku.txt _ __ file
#     ?.w.. "Here's one more haiku\n"
#     ?.w.. "What about the older one?\n"
#     ?.w.. "Let's go check it out"
#
# # a - appends to end, preserving original contents
# # NO CONTROL OVER CURSOR
#
# w__ o.. haiku.txt _ __ file
#     ?.s.. 0
#     ?.w.. ":)\n"
#
# # r+ read and write
# w__ o.. haiku.txt __ __ file
#     ?.w.. ":)"
#     ?.s.. 10
#     ?.w.. ":("
# # r+ will not create a file if it doesn't exist
# w__ o.. hello.txt _ __ file
#     ?.w.. HELLO!!!
