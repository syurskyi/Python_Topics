# c_ HtmlElement
#     indent_size _ 2
#
#     ___  - ____ name_"" text_""
#         ____.? ?
#         ____.? ?
#         ____.elements _      # list
#
#     ___ __str ____ indent
#         lines _    # list
#         i _ ' ' * i... * ____.i..
#         l__.a.. _* ? < ____.n.. >*
#
#         __ ____.t..
#             i1 _ ' ' * i.. + 1) * ____.i..
#             l__.a..  _* ? ____.t..
#
#         ___ e __ ____.e..
#             l__.a.. ?.__st. i.. + 1
#
#         l__.a..  _* ? </ ____.n.. >
#         r_ '\n'.j.. l..
#
#     ___ -s ____
#         r_ ____.__st. 0
#
#     ?s
#     ___ create name
#         r_ H.. ?
#
#
# c_ HtmlBuilder:
#     __root _ H..
#
#     ___  - ____ root_name
#         ____.?  ?
#         ____.__r__.n__ _ r..
#
#     # not fluent
#     ___ add_child ____ child_name child_text
#         ____.__r__.e__.a..(
#             H.. ? ?
#         )
#
#     # fluent
#     ___ add_child_fluen ____ child_name child_text
#         ____.__r__.e__.a..(
#             H.. ? ?
#         )
#         r_ ____
#
#     ___ clear ____
#         ____.__r.. _ H.. name_self.root_name
#
#     ___ -s ____
#         r_ st. ____.__r..
#
#
# # __ you want to build a simple HTML paragraph using a list
# hello _ 'hello'
# parts _ ['<p>', hello, '</p>']
# print(''.join(parts))
#
# # now I want an HTML list with 2 words __ it
# words _ ['hello', 'world']
# parts _ ['<ul>']
# ___ w __ words:
#     parts.a..( _*  <li>{w}</li>')
# parts.a..('</ul>')
# print('\n'.join(parts))
#
# # ordinary non-fluent builder
# # builder _ HtmlBuilder('ul')
# builder _ HtmlElement.create('ul')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')
# print('Ordinary builder:')
# print(builder)
#
# # fluent builder
# builder.clear()
# builder.add_child_fluent('li', 'hello') \
#     .add_child_fluent('li', 'world')
# print('Fluent builder:')
# print(builder)
